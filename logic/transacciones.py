from database.db_manager import DatabaseManager


class TransaccionesManager:
    def __init__(self):
        self.db = DatabaseManager()
    
    def depositar(self, usuario_id, monto):
        """Deposita dinero en la cuenta del usuario"""
        try:
            if monto <= 0:
                return {"exito": False, "mensaje": "El monto debe ser mayor a 0"}
            
            usuario = self.db.obtener_usuario_por_id(usuario_id)
            if not usuario:
                return {"exito": False, "mensaje": "Usuario no encontrado"}
            
            nuevo_saldo = usuario["saldo"] + monto
            self.db.actualizar_saldo(usuario_id, nuevo_saldo)
            
            self.db.registrar_transaccion(
                usuario_id=usuario_id,
                tipo="DEPOSITO",
                monto=monto,
                descripcion=f"Depósito de ${monto:,.2f}"
            )
            
            return {
                "exito": True,
                "mensaje": f"Depósito exitoso de ${monto:,.2f}",
                "nuevo_saldo": nuevo_saldo
            }
        except Exception as e:
            return {"exito": False, "mensaje": f"Error: {str(e)}"}
    
    def retirar(self, usuario_id, monto):
        """Retira dinero de la cuenta del usuario"""
        try:
            if monto <= 0:
                return {"exito": False, "mensaje": "El monto debe ser mayor a 0"}
            
            usuario = self.db.obtener_usuario_por_id(usuario_id)
            if not usuario:
                return {"exito": False, "mensaje": "Usuario no encontrado"}
            
            if usuario["saldo"] < monto:
                return {"exito": False, "mensaje": "Saldo insuficiente"}
            
            nuevo_saldo = usuario["saldo"] - monto
            self.db.actualizar_saldo(usuario_id, nuevo_saldo)
            
            self.db.registrar_transaccion(
                usuario_id=usuario_id,
                tipo="RETIRO",
                monto=monto,
                descripcion=f"Retiro de ${monto:,.2f}"
            )
            
            return {
                "exito": True,
                "mensaje": f"Retiro exitoso de ${monto:,.2f}",
                "nuevo_saldo": nuevo_saldo
            }
        except Exception as e:
            return {"exito": False, "mensaje": f"Error: {str(e)}"}
    
    def transferir(self, usuario_origen_id, usuario_destino, monto):
        """Transfiere dinero a otro usuario"""
        try:
            if monto <= 0:
                return {"exito": False, "mensaje": "El monto debe ser mayor a 0"}
            
            usuario_origen = self.db.obtener_usuario_por_id(usuario_origen_id)
            if not usuario_origen:
                return {"exito": False, "mensaje": "Usuario origen no encontrado"}
            
            if usuario_origen["saldo"] < monto:
                return {"exito": False, "mensaje": "Saldo insuficiente"}
            
            usuario_destino_data = self.db.obtener_usuario_por_nombre(usuario_destino)
            if not usuario_destino_data:
                return {"exito": False, "mensaje": "Usuario destino no encontrado"}
            
            if usuario_origen_id == usuario_destino_data["id"]:
                return {"exito": False, "mensaje": "No puedes transferirte a ti mismo"}
            
            nuevo_saldo_origen = usuario_origen["saldo"] - monto
            nuevo_saldo_destino = usuario_destino_data["saldo"] + monto
            
            self.db.actualizar_saldo(usuario_origen_id, nuevo_saldo_origen)
            self.db.actualizar_saldo(usuario_destino_data["id"], nuevo_saldo_destino)
            
            self.db.registrar_transaccion(
                usuario_id=usuario_origen_id,
                tipo="TRANSFERENCIA_ENVIADA",
                monto=monto,
                destinatario_id=usuario_destino_data["id"],
                descripcion=f"Transferencia a {usuario_destino}"
            )
            
            self.db.registrar_transaccion(
                usuario_id=usuario_destino_data["id"],
                tipo="TRANSFERENCIA_RECIBIDA",
                monto=monto,
                destinatario_id=usuario_origen_id,
                descripcion=f"Transferencia de {usuario_origen['usuario']}"
            )
            
            return {
                "exito": True,
                "mensaje": f"Transferencia exitosa de ${monto:,.2f} a {usuario_destino}",
                "nuevo_saldo": nuevo_saldo_origen
            }
        except Exception as e:
            return {"exito": False, "mensaje": f"Error: {str(e)}"}
    
    def consultar_saldo(self, usuario_id):
        """Consulta el saldo actual del usuario"""
        try:
            usuario = self.db.obtener_usuario_por_id(usuario_id)
            if not usuario:
                return {"exito": False, "mensaje": "Usuario no encontrado"}
            
            return {
                "exito": True,
                "saldo": usuario["saldo"],
                "usuario": usuario["usuario"]
            }
        except Exception as e:
            return {"exito": False, "mensaje": f"Error: {str(e)}"}
    
    def obtener_historial(self, usuario_id, limite=20):
        """Obtiene el historial de transacciones"""
        try:
            transacciones = self.db.obtener_transacciones(usuario_id, limite)
            return {
                "exito": True,
                "transacciones": transacciones
            }
        except Exception as e:
            return {"exito": False, "mensaje": f"Error: {str(e)}"}
