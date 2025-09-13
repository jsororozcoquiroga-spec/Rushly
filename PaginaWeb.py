import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Rushly - Innovación en Movimiento",
    page_icon="🚗",
    layout="centered"
)

# Hero con logo
st.image("Logo.png", width=200)
st.markdown("<h1 style='text-align: center; color: #0d47a1;'>Rushly 🚗</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:20px;'><i>“Innovación que mueve el futuro”</i></p>", unsafe_allow_html=True)

st.markdown("---")

# Sobre el proyecto
st.header("Sobre el Proyecto")
st.write("""
Rushly es un vehículo innovador diseñado con un enfoque en la **sostenibilidad, eficiencia y tecnología avanzada**.  
Su desarrollo integra diseño mecánico, electrónico y sistemas inteligentes para transformar la movilidad.
""")

# Características
st.header("Características Clave")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("⚡ Eficiencia Energética")
    st.write("Optimizado para reducir consumo y maximizar el rendimiento.")

with col2:
    st.subheader("🌱 Sostenibilidad")
    st.write("Diseñado con materiales eco-amigables y procesos responsables.")

with col3:
    st.subheader("🤖 Tecnología Inteligente")
    st.write("Integración de sistemas avanzados para control y seguridad.")

st.markdown("---")

# Equipo
st.header("Nuestro Equipo")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://via.placeholder.com/150", width=120)
    st.subheader("Cesar David Chacón Landinez")
    st.caption("Lider Del Proyecto")

with col2:
    st.image("https://via.placeholder.com/150", width=120)
    st.subheader("Guisella Valentina Restrepo Sinisterra")
    st.caption("Software & IA")

with col3:
    st.image("https://via.placeholder.com/150", width=120)
    st.subheader("Julián David Carvajal Donoso")
    st.caption("Software & IA")

col4, col5, col6 = st.columns(3)

with col4:
    st.image("https://via.placeholder.com/150", width=120)
    st.subheader("Juan Sebastián Orozco Quiroga")
    st.caption("Diseñador Mecánico")

with col5:
    st.image("https://via.placeholder.com/150", width=120)
    st.subheader("Santiago Fernandez Yazo")
    st.caption("Diseñador Electrónico")

with col6:
    st.image("https://via.placeholder.com/150", width=120)
    st.subheader("Juan David Ríos Muñoz")
    st.caption("Diseñador Del Control")

st.markdown("---")

# Roadmap
st.header("Roadmap del Proyecto")

with st.expander("✅ Fase 1: Diseño Conceptual"):
    st.write("""
    En esta fase se definió la idea inicial del vehículo, sus subsistemas y se evaluaron diferentes alternativas.
    """)

with st.expander("🔄 Fase 2: Desarrollo de Prototipo"):
    st.write("""
    Construcción del primer prototipo físico y validación de componentes clave.
    """)

with st.expander("⏳ Fase 3: Pruebas y Validaciones"):
    st.write("""
    Se realizan pruebas en distintos escenarios para garantizar la seguridad, eficiencia y robustez del sistema.
    """)

with st.expander("🚀 Fase 4: Resultado Final"):
    st.write("""
    Despues de todas las pruebas y ajustes realizados, Rushly a quedado de la siguiente manera.
    """)


st.markdown("---")

# Contacto
st.header("Únete al Futuro")
st.write("¿Quieres saber más sobre Rushly? Contáctanos y forma parte de la innovación.")
st.markdown("📩 [Escríbenos](mailto:info@rushly.com)")

# Footer
st.markdown("<br><hr><p style='text-align:center;'>© 2025 Rushly. Todos los derechos reservados.</p>", unsafe_allow_html=True)
