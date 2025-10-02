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

st.markdown("---")

# Características
st.header("Características Clave")

with st.expander("⚡ Eficiencia Energética"):
    st.write("Optimizado para reducir consumo y maximizar el rendimiento.")

with st.expander("🌱 Sostenibilidad"):
    st.write("Diseñado con materiales eco-amigables y procesos responsables.")

with st.expander("🤖 Tecnología Inteligente"):
    st.write("Integración de sistemas avanzados para control y seguridad.")

st.markdown("---")

# Equipo
st.header("Nuestro Equipo")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://via.placeholder.com/150", width=120)
    st.subheader("Cesar David Chacón Landinez")
    st.caption("Líder del Proyecto")

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
    st.caption("Diseñador del Control")

st.markdown("---")

# Roadmap
st.header("Roadmap del Proyecto")

with st.expander("✅ Fase 1: Diseño Conceptual"):
    st.write("""
    En esta fase se definió la **idea inicial del vehículo Rushly**, estableciendo su justificación, objetivos y alcance.  
    Se planteó como un proyecto orientado a la **movilidad sostenible**, integrando innovación tecnológica con eficiencia energética.  
    """)

    with st.expander("📌 Justificación del Proyecto"):
        st.write("""
        Rushly nace como respuesta a la necesidad de **movilidad sostenible e inteligente**, integrando innovación tecnológica con eficiencia energética.  
        El proyecto busca demostrar que es posible desarrollar soluciones de transporte respetuosas con el medio ambiente y, al mismo tiempo, accesibles y confiables.
        """)

    with st.expander("🎯 Objetivos del Proyecto"):
        st.write("""
        - **Objetivo General:** Desarrollar un prototipo de vehículo innovador enfocado en sostenibilidad, eficiencia y tecnología inteligente.  
        - **Objetivos Específicos:**  
          - Integrar sensores avanzados para control y seguridad.  
          - Optimizar el consumo energético de los sistemas.  
          - Diseñar software de gestión y monitoreo.  
          - Validar el prototipo en escenarios de prueba.  
        """)

    with st.expander("📊 Encuesta Previa"):
        st.write("""
        Para la construcción de los primeros **bocetos del vehículo** y la definición de los subsistemas,  
        se aplicó una encuesta con el fin de recopilar información sobre **preferencias, expectativas y necesidades** relacionadas con la movilidad sostenible.  
        Los resultados de esta encuesta orientaron las decisiones de diseño y priorización de funcionalidades.  
        """)

    with st.expander("🧩 Subsistemas del Proyecto"):
        st.write("""
        Rushly se concibe como un sistema integrado compuesto por diversos **subsistemas**:  
        - **Subsistema Mecánico:** estructura, chasis y elementos de transmisión.  
        - **Subsistema Electrónico:** sensores, actuadores y placas de control.  
        - **Subsistema de Software:** algoritmos de monitoreo, control y comunicación.  
        - **Subsistema de Control:** estrategias para garantizar estabilidad, seguridad y eficiencia en la movilidad.  

        Estos subsistemas fueron mapeados para visualizar su interacción y dependencia.
        """)

        # Línea para mostrar el mapa de subsistemas (cambia "MapaSubsistemas.png" por el nombre del archivo que subas)
        st.image("SistemaYSubsistema.png", caption="Mapa de Subsistemas de Rushly", use_column_width=True)

    with st.expander("📍 Alcance Inicial"):
        st.write("""
        En la fase inicial, Rushly se centra en el **diseño conceptual y prototipado básico**, incorporando sistemas electrónicos, mecánicos y de control.  
        También se ejecutan pruebas preliminares de hardware y software, que servirán como base para futuras etapas de validación y escalamiento del proyecto.
        """)

    with st.expander("✅ Viabilidad y Beneficios"):
        st.write("""
        Rushly aporta beneficios tanto en el ámbito académico como en el tecnológico.  
        Para el equipo, representa un espacio de **aprendizaje y aplicación práctica** de conocimientos en ingeniería mecatrónica.  
        A nivel social, promueve una visión de **movilidad más limpia y eficiente**, con potencial de inspirar desarrollos similares en el futuro.
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
    Después de todas las pruebas y ajustes realizados, Rushly ha quedado de la siguiente manera.
    """)

st.markdown("---")

# Contacto
st.header("Únete al Futuro")
st.write("¿Quieres saber más sobre Rushly? Contáctanos y forma parte de la innovación.")
st.markdown("📩 [Escríbenos](mailto:info@rushly.com)")

# Footer
st.markdown("<br><hr><p style='text-align:center;'>© 2025 Rushly. Todos los derechos reservados.</p>", unsafe_allow_html=True)
