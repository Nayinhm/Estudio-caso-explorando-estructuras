
from .material import Material

class BibliotecaSystem:
    """Clase que administra la lógica del sistema mediante listas, pilas y colas."""
    def __init__(self):
        self.inventario = []         # Lista para el inventario de materiales
        self.cola_solicitudes = []   # Cola (FIFO) para las solicitudes de préstamo
        self.pila_operaciones = []   # Pila (LIFO) para el historial de operaciones

    # --- 1. ADMINISTRACIÓN DEL INVENTARIO (LISTAS) ---
    def registrar_material(self):
        print("\n--- Registrar Nuevo Material ---")
        codigo = input("Ingrese el código del material: ").strip()
        
        # Validar existencia previa
        for mat in self.inventario:
            if mat.codigo == codigo:
                print("⚠️ Error: Ya existe un material registrado con ese código.")
                return

        titulo = input("Ingrese el título: ").strip()
        autor = input("Ingrese el autor: ").strip()
        
        nuevo_material = Material(codigo, titulo, autor, "disponible")
        self.inventario.append(nuevo_material)
        
        # Registrar operación en la pila
        self.pila_operaciones.append(f"Se registró el material: {titulo} ({codigo})")
        print("✅ Material registrado exitosamente.")

    def consultar_materiales(self):
        print("\n--- Inventario de Materiales ---")
        if not self.inventario:
            print("📭 El inventario está vacío.")
            return
        for i, mat in enumerate(self.inventario, 1):
            print(f"{i}. {mat}")

    def buscar_material_por_codigo(self):
        print("\n--- Buscar Material por Código ---")
        if not self.inventario:
            print("📭 El inventario está vacío.")
            return
        codigo = input("Ingrese el código a buscar: ").strip()
        for mat in self.inventario:
            if mat.codigo == codigo:
                print(f"🔍 Material encontrado:\n   {mat}")
                return
        print("❌ No se encontró ningún material con ese código.")

    def modificar_material(self):
        print("\n--- Modificar Material ---")
        if not self.inventario:
            print("📭 El inventario está vacío.")
            return
        codigo = input("Ingrese el código del material a modificar: ").strip()
        for mat in self.inventario:
            if mat.codigo == codigo:
                print(f"Material actual: {mat}")
                mat.titulo = input(f"Nuevo título [{mat.titulo}]: ").strip() or mat.titulo
                mat.autor = input(f"Nuevo autor [{mat.autor}]: ").strip() or mat.autor
                
                self.pila_operaciones.append(f"Se modificó el material con código {codigo}")
                print("✅ Material modificado exitosamente.")
                return
        print("❌ No se encontró ningún material con ese código.")

    def eliminar_material(self):
        print("\n--- Eliminar Material ---")
        if not self.inventario:
            print("📭 El inventario está vacío.")
            return
        codigo = input("Ingrese el código del material a eliminar: ").strip()
        for mat in self.inventario:
            if mat.codigo == codigo:
                self.inventario.remove(mat)
                self.pila_operaciones.append(f"Se eliminó el material con código {codigo}")
                print("🗑️ Material eliminado exitosamente.")
                return
        print("⚠️ Error: No se puede eliminar. El material no existe en el inventario.")

    # --- 2. GESTIÓN DE SOLICITUDES DE PRÉSTAMO (COLAS - FIFO) ---
    def registrar_solicitud(self):
        print("\n--- Registrar Solicitud de Préstamo ---")
        if not self.inventario:
            print("📭 No hay materiales en el inventario para solicitar.")
            return
        
        codigo = input("Ingrese el código del material solicitado: ").strip()
        material_encontrado = None
        for mat in self.inventario:
            if mat.codigo == codigo:
                material_encontrado = mat
                break
        
        if not material_encontrado:
            print("❌ El material no existe en el inventario.")
            return
        
        if material_encontrado.estado == "prestado":
            print("ℹ️ El material ya está prestado. Se agregará a la cola de espera.")
        
        estudiante = input("Ingrese el nombre del estudiante: ").strip()
        solicitud = {"estudiante": estudiante, "codigo_material": codigo, "titulo": material_encontrado.titulo}
        
        self.cola_solicitudes.append(solicitud)  # Encolar (Enqueue)
        self.pila_operaciones.append(f"Solicitud registrada para {estudiante} (Material: {codigo})")
        print("✅ Solicitud agregada a la cola de espera exitosamente.")

    def consultar_solicitudes_pendientes(self):
        print("\n--- Solicitudes Pendientes (Cola) ---")
        if not self.cola_solicitudes:
            print("📭 No hay solicitudes pendientes en la cola.")
            return
        for i, sol in enumerate(self.cola_solicitudes, 1):
            print(f"{i}. Estudiante: {sol['estudiante']} | Material: {sol['titulo']} (Código: {sol['codigo_material']})")

    def atender_primera_solicitud(self):
        print("\n--- Atender Primera Solicitud ---")
        if not self.cola_solicitudes:
            print("⚠️ Error: La cola de solicitudes está vacía. No hay turnos por atender.")
            return
        
        # Desencolar (Dequeue) al primer elemento (FIFO)
        solicitud_atendida = self.cola_solicitudes.pop(0)
        
        for mat in self.inventario:
            if mat.codigo == solicitud_atendida["codigo_material"]:
                mat.estado = "prestado"
                break

        self.pila_operaciones.append(f"Se atendió solicitud de {solicitud_atendida['estudiante']} para material {solicitud_atendida['codigo_material']}")
        print(f"🎉 Atendiendo a: {solicitud_atendida['estudiante']} para el material '{solicitud_atendida['titulo']}'.")

    # --- 3. CONTROL DE OPERACIONES RECIENTES (PILAS - LIFO) ---
    def consultar_ultima_operacion(self):
        print("\n--- Consultar Última Operación (Pila) ---")
        if not self.pila_operaciones:
            print("⚠️ Error: La pila de operaciones está sin registros.")
            return
        print(f"⏱️ Última operación registrada: {self.pila_operaciones[-1]}")

    def retirar_ultima_operacion(self):
        print("\n--- Retirar Operación Reciente ---")
        if not self.pila_operaciones:
            print("⚠️ Error: La pila está vacía, no hay operaciones que retirar.")
            return
        operacion_retirada = self.pila_operaciones.pop()  # Desapilar (Pop)
        print(f"🔙 Operación retirada de la pila: '{operacion_retirada}'")

    # --- 4. CONSULTA GENERAL DE INFORMACIÓN ---
    def consulta_general(self):
        print("\n========================================")
        print("          CONSULTA GENERAL              ")
        print("========================================")
        print(f"📚 Cantidad total de materiales: {len(self.inventario)}")
        
        disponibles = sum(1 for m in self.inventario if m.estado == "disponible")
        prestados = sum(1 for m in self.inventario if m.estado == "prestado")
        print(f"   - Disponibles: {disponibles}")
        print(f"   - Prestados: {prestados}")
        
        print(f"⏳ Solicitudes pendientes en cola: {len(self.cola_solicitudes)}")
        print(f"⏱️ Operaciones registradas en pila: {len(self.pila_operaciones)}")
        print("========================================")