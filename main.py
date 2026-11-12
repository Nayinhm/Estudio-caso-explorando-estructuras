
from clases.biblioteca import BibliotecaSystem

def main():
    app = BibliotecaSystem()
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE BIBLIOTECA ===")
        print("1. Registrar nuevo material (Lista)")
        print("2. Consultar inventario de materiales (Lista)")
        print("3. Buscar material por código (Lista)")
        print("4. Modificar información de material (Lista)")
        print("5. Eliminar material del inventario (Lista)")
        print("6. Registrar solicitud de préstamo (Cola)")
        print("7. Consultar solicitudes pendientes (Cola)")
        print("8. Atender primera solicitud de préstamo (Cola)")
        print("9. Consultar última operación realizada (Pila)")
        print("10. Retirar operación más reciente (Pila)")
        print("11. Consulta general del sistema")
        print("12. Salir")
        
        opcion = input("Seleccione una opción (1-12): ").strip()
        
        if opcion == "1":
            app.registrar_material()
        elif opcion == "2":
            app.consultar_materiales()
        elif opcion == "3":
            app.buscar_material_por_codigo()
        elif opcion == "4":
            app.modificar_material()
        elif opcion == "5":
            app.eliminar_material()
        elif opcion == "6":
            app.registrar_solicitud()
        elif opcion == "7":
            app.consultar_solicitudes_pendientes()
        elif opcion == "8":
            app.atender_primera_solicitud()
        elif opcion == "9":
            app.consultar_ultima_operacion()
        elif opcion == "10":
            app.retirar_ultima_operacion()
        elif opcion == "11":
            app.consulta_general()
        elif opcion == "12":
            print("\n👋 Saliendo del sistema de biblioteca. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción inválida. Por favor, ingrese un número del 1 al 12.")

if __name__ == "__main__":
    main()