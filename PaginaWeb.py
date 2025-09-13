import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Rushly - Innovación en Movimiento",
    page_icon="🚗",
    layout="centered"
)

# Hero section
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

# Contacto
st.header("Únete al Futuro")
st.write("¿Quieres saber más sobre Rushly? Contáctanos y forma parte de la innovación.")
st.markdown("📩 [Escríbenos](mailto:info@rushly.com)")

st.markdown("<br><hr><p style='text-align:center;'>© 2025 Rushly. Todos los derechos reservados.</p>", unsafe_allow_html=True)
