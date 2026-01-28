"""
Sistema de Pedidos de Restaurante con Delivery
"""

# ===== BASE DE DATOS DEL RESTAURANTE =====

# Menú del restaurante organizado por categorías
menu = {
    "entradas": {
        "Nachos": {"precio": 8.50, "tiempo": 10, "puntos": 50},
        "Alitas BBQ": {"precio": 12.00, "tiempo": 15, "puntos": 80},
        "Ensalada César": {"precio": 9.00, "tiempo": 8, "puntos": 60},
        "Croquetas": {"precio": 7.50, "tiempo": 12, "puntos": 45}
    },
    "principales": {
        "Pizza Margherita": {"precio": 15.00, "tiempo": 20, "puntos": 100},
        "Pizza Pepperoni": {"precio": 16.50, "tiempo": 20, "puntos": 110},
        "Hamburguesa Clásica": {"precio": 13.50, "tiempo": 18, "puntos": 90},
        "Hamburguesa BBQ": {"precio": 14.50, "tiempo": 18, "puntos": 95},
        "Pasta Carbonara": {"precio": 14.00, "tiempo": 15, "puntos": 95},
        "Pasta Bolognesa": {"precio": 13.00, "tiempo": 15, "puntos": 85}
    },
    "postres": {
        "Helado": {"precio": 5.00, "tiempo": 2, "puntos": 30},
        "Tarta de Queso": {"precio": 6.50, "tiempo": 3, "puntos": 40},
        "Brownie": {"precio": 5.50, "tiempo": 3, "puntos": 35},
        "Flan": {"precio": 4.50, "tiempo": 2, "puntos": 25}
    },
    "bebidas": {
        "Refresco": {"precio": 3.00, "tiempo": 1, "puntos": 15},
        "Agua": {"precio": 2.00, "tiempo": 1, "puntos": 10},
        "Jugo Natural": {"precio": 4.50, "tiempo": 3, "puntos": 25},
        "Café": {"precio": 2.50, "tiempo": 2, "puntos": 15}
    }
}

# Base de datos de clientes VIP con puntos acumulados
clientes_vip = {
    "juan": {"puntos": 500, "pedidos": 12},
    "maria": {"puntos": 1200, "pedidos": 28},
    "pedro": {"puntos": 300, "pedidos": 7},
    "ana": {"puntos": 850, "pedidos": 19},
    "luis": {"puntos": 150, "pedidos": 3}
}

# Combos especiales del día (sets para los items)
combos_del_dia = {
    "Combo Italiano": {
        "items": {"Pizza Margherita", "Refresco"},
        "descuento": 15  # Porcentaje de descuento
    },
    "Combo Burger": {
        "items": {"Hamburguesa Clásica", "Nachos", "Refresco"},
        "descuento": 20
    },
    "Combo Light": {
        "items": {"Ensalada César", "Agua", "Flan"},
        "descuento": 10
    }
}

# ====== Funciones del sistema =============

def mostrar_bienvenida():
    # muestra el mensaje de bienvenida
    print("=" * 60)
    print("=" * 15 + "🍕 ¡Bienvenido a Python Eats! 🍕")
    print("=" * 60)
    print()

def verificar_cliente():
    es_cliente = ""
    while es_cliente not in ["s","si","n","no"]:
        es_cliente = input("¿Eres cliente registrado? (s/n): ")
        if es_cliente not in ["s","si","n","no"]:
            print(" Por favor, ingresa 's' para si 'n' para no.")
    if es_cliente in ["s","si"]:
        nombre = input("Ingresa tu nombre: ")

        if nombre in clientes_vip:
            puntos = clientes_vip[nombre]["puntos"]
            print(f"\n✨ ¡Hola {nombre}! Tienes {puntos} puntos acumulados.")
            print(f"📊 Has realizado {clientes_vip[nombre]['pedidos']} pedidos con nosotros.")
            return nombre, puntos, True
        else:
            print(f"\n👋 Hola {nombre}! No estás registrado como cliente VIP.")
            print("Te registraremos automáticamente después de tu pedido.")
            return nombre, 0, False
        
    else:
        print("\n👋 ¡Bienvenido nuevo cliente!")
        nombre = input("¿Como te llamas? ")
        print(f"    Gracias {nombre}, te registraremos después del pedido.")
        return nombre, 0, False