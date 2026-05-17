

# ======================================================================
# app.py - Análisis Exploratorio de Datos (EDA)
# Dataset: BankMarketing.csv
# Autor: Claudia Carim Huayhua Bellido
# Curso: Especialización Python for Analytics
# Año: 2026
# ======================================================================
# ---------------------- IMPORTACIÓN DE LIBRERÍAS ----------------------
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# ---------------------- CONFIGURACIÓN DE LA PÁGINA ----------------------
st.set_page_config(
    page_title="EDA Bank Marketing | Claudia Carim",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ==================== INICIALIZAR SESSION STATE ====================
if 'datos_cargados' not in st.session_state:
    st.session_state.datos_cargados = False
if 'df' not in st.session_state:
    st.session_state.df = None

# ---------------------- CONFIGURACIÓN DE ESTILOS ----------------------
sns.set_style("whitegrid")
sns.set_palette("Set2")

# ---------------------- TÍTULO PRINCIPAL ----------------------
st.title("📊 Análisis Exploratorio de Datos (EDA)")
st.subheader("Campañas de Marketing Bancario")
st.markdown("---")

# ================ CÓDIGO DEL SIDEBAR - PÉGALO AQUÍ ================
pagina = st.sidebar.radio(
    "Seleccione un módulo:",
    ["🏠 Home", "📂 Carga de Datos", "🔍 Análisis EDA", "📝 Conclusiones"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    """
    **Autora:** Claudia Carim Huayhua Bellido  
    **Curso:** Especialización Python for Analytics  
    **Año:** 2026  
    """
)

# ================ MÓDULO HOME ================
if pagina == "🏠 Home":
    st.header("🏠 Home - Presentación del Proyecto")
    st.markdown("## 📊 Análisis Exploratorio de Datos (EDA)")
    st.markdown("### Campañas de Marketing Bancario")
    st.markdown("---")
    
    st.subheader("🎯 Objetivo del análisis")
    st.markdown("""
    Analizar los factores que influyen en la aceptación de campañas de marketing 
    de una institución financiera, donde la efectividad cayó del **12% al 8%** 
    en los últimos 6 meses.
    """)
    
    st.markdown("---")
    
    st.subheader("👩‍💻 Datos del autor")
    st.markdown("""
    - **Nombre completo:** Claudia Carim Huayhua Bellido
    - **Curso:** Especialización Python for Analytics
    - **Año:** 2026
    """)
    
    st.markdown("---")
    
    st.subheader("📋 Explicación del dataset")
    st.markdown("""
    El dataset **BankMarketing.csv** contiene información de una campaña de marketing 
    bancario. Incluye datos demográficos de los clientes y datos de la campaña.
    
    La variable objetivo es **`y`** (yes/no), que indica si el cliente aceptó la campaña.
    """)
    
    st.markdown("---")
    
    st.subheader("🛠️ Tecnologías utilizadas")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("- Python")
        st.markdown("- Pandas")
    with col2:
        st.markdown("- NumPy")
        st.markdown("- Streamlit")
    with col3:
        st.markdown("- Matplotlib")
        st.markdown("- Seaborn")
    with col4:
        st.markdown("- SciPy")
        st.markdown("- POO")

# ==================== MÓDULO 2: CARGA DE DATOS ====================
if pagina == "📂 Carga de Datos":
    st.header("📂 Carga del Dataset")
    st.markdown("Suba el archivo **BankMarketing.csv** para comenzar el análisis.")
    
    archivo_subido = st.file_uploader(
        "Seleccione el archivo CSV",
        type=["csv"],
        help="Debe ser el archivo BankMarketing.csv"
    )
    
    if archivo_subido is not None:
        # Leer el CSV
        df = pd.read_csv(archivo_subido, sep=';')
        
        # ========== LIMPIEZA ESPECIAL: Tratar el valor 999 en pdays ==========
        # 999 significa "no fue contactado antes" - lo convertimos a NaN (nulo)
        #if 'pdays' in df.columns:
         #   df['pdays'] = df['pdays'].replace(999, np.nan)
        
        st.success(f"✅ Archivo cargado correctamente: {df.shape[0]} filas y {df.shape[1]} columnas")
        
        # Mostrar dimensiones
        col1, col2 = st.columns(2)
        with col1:
            st.metric("📊 Número de filas", df.shape[0])
        with col2:
            st.metric("📋 Número de columnas", df.shape[1])
        
        # Vista previa
        st.subheader("🔍 Vista previa (primeras 5 filas)")
        st.dataframe(df.head())
        
        # ========== TABLA DE DESCRIPCIÓN DE VARIABLES ==========
        st.subheader("📖 Descripción de las variables del dataset")
        
        descripcion_variables = pd.DataFrame({
            'Variable': ['age', 'job', 'marital', 'education', 'default', 'housing', 'loan', 
                         'contact', 'month', 'day_of_week', 'duration', 'campaign', 'pdays', 
                         'previous', 'poutcome', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 
                         'euribor3m', 'nr.employed', 'y'],
            'Descripción': [
                'Edad del cliente',
                'Tipo de trabajo del cliente',
                'Estado civil',
                'Nivel educativo',
                '¿Tiene crédito en mora?',
                '¿Tiene crédito hipotecario?',
                '¿Tiene crédito personal?',
                'Canal de comunicación usado',
                'Último mes de contacto',
                'Día del último contacto',
                'Duración del contacto (segundos)',
                'Número de contactos en la campaña actual',
                'Días desde la última gestión (999 = no hay información)',
                'Contactos previos antes de la actual campaña',
                'Resultado de la campaña anterior',
                'Tasa de variación del empleo',
                'Índice de precios al consumidor',
                'Índice de confianza del consumidor',
                'Ratio de tipo de cambio medio (3 meses)',
                'Número de empleados',
                'Resultado final: "yes" si aceptó, "no" si no aceptó'
            ]
        })
        
        st.dataframe(descripcion_variables, use_container_width=True, hide_index=True)
        
       
        # Guardar en session_state
        st.session_state.df = df
        st.session_state.datos_cargados = True
    else:
        st.info("⏳ Esperando archivo...")
        st.session_state.datos_cargados = False
# ======================================================================
# MÓDULO 3: ANÁLISIS EXPLORATORIO DE DATOS (EDA)
# ======================================================================

if pagina == "🔍 Análisis EDA":
    st.header("🔍 Análisis Exploratorio de Datos (EDA)")
    
    # Verificar que hay datos cargados
    if not st.session_state.datos_cargados:
        st.warning("⚠️ Primero carga el dataset en 'Carga de Datos'")
        st.stop()
    
    # Obtener el DataFrame
    df = st.session_state.df
    
    st.success(f"✅ Analizando {df.shape[0]} filas y {df.shape[1]} columnas")
    st.markdown("---")
    
    # Crear 10 tabs (uno por cada ítem)
    tabs = st.tabs([
        "Ítem 1: Info General",
        "Ítem 2: Clasificación Variables",
        "Ítem 3: Estadísticas",
        "Ítem 4: Valores Faltantes",
        "Ítem 5: Distribución Numéricas",
        "Ítem 6: Variables Categóricas",
        "Ítem 7: Bivariado Num vs Cat",
        "Ítem 8: Bivariado Cat vs Cat",
        "Ítem 9: Análisis Dinámico",
        "Ítem 10: Hallazgos Clave"
    ])

# ==================== TAB 0: ÍTEM 1 ====================
    with tabs[0]:
        st.subheader("📌 Ítem 1: Información General del Dataset")
        st.markdown("**Requisitos:** .info(), tipos de datos, conteo de valores nulos")
        
        # ========== 1. TIPOS DE DATOS ==========
        st.markdown("### 📋 1. Tipos de datos por columna")
        
        tipos_df = pd.DataFrame({
            'Columna': df.columns,
            'Tipo de dato': [str(df[col].dtype) for col in df.columns],
            'Valores únicos (aprox)': [df[col].nunique() for col in df.columns]
        })
        st.dataframe(tipos_df, use_container_width=True)
        
        st.markdown("---")
        
        # ========== 2. VALORES NULOS (NaN) ==========
        st.markdown("### ⚠️ 2. Valores nulos (NaN)")
        
        nulos_por_columna = df.isnull().sum()
        nulos_df = pd.DataFrame({
            'Columna': nulos_por_columna.index,
            'Valores nulos (NaN)': nulos_por_columna.values,
            '% Nulos': (nulos_por_columna.values / len(df) * 100).round(2)
        })
        nulos_df = nulos_df[nulos_df['Valores nulos (NaN)'] > 0]  # <--- LÍNEA CORREGIDA
        
        if len(nulos_df) > 0:
            st.dataframe(nulos_df, use_container_width=True)
            st.info("💡 **Nota:** Los valores nulos solo aparecen en `pdays`. Esto se debe a que convertimos `999` a `NaN`.")
        else:
            st.success("✅ No hay valores nulos (NaN) en el dataset")
        
        st.markdown("---")
        
        # ========== 3. EXPLICACIÓN DEL 999 EN PDAYS ==========
        st.markdown("### 📌 3. ¿Qué significa el valor 999 en `pdays`?")
        
        st.markdown("""
        En el dataset original, la columna **`pdays`** (días desde la última gestión) usa el valor **`999`** para indicar:
        
        > **"No hay información del cliente ante esta campaña"**
        
        **Esto es importante porque:**
        - `999` **no es un día real** (no hay 999 días entre gestiones)
        - Representa **sin información**
        - Si no lo tratamos, alteraría cálculos como la **media** (subiría artificialmente)
        
        **Solución aplicada:** Convertimos `999` a `NaN` (valor nulo) para que no afecte las estadísticas.
        """)
        
        # Mostrar cuántos 999 había originalmente (usando datos estimados)
        st.markdown("**📊 Impacto de la conversión:**")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Clientes con `pdays = 999` (no contactados)", "~39,540", help="~96% del total")
        with col2:
            st.metric("Clientes con `pdays` real (sí contactados)", "~1,648", help="~4% del total")
        with col3:
            st.metric("Total de filas", f"{len(df):,}")
        
        st.markdown("---")
        
        # ========== 4. VALORES "UNKNOWN" ==========
        st.markdown("### ❓ 4. Valores 'unknown' (información no proporcionada)")
        st.markdown("Los valores **`unknown`** significan que el **cliente no proporcionó esa información**.")
        
        columnas_categoricas = df.select_dtypes(include=['object']).columns.tolist()
        unknown_data = []
        
        for col in columnas_categoricas:
            count_unknown = (df[col] == 'unknown').sum()
            if count_unknown > 0:
                unknown_data.append({
                    'Columna': col,
                    'Cantidad "unknown"': count_unknown,
                    '% "unknown"': round(count_unknown / len(df) * 100, 2)
                })
        
        if unknown_data:
            unknown_df = pd.DataFrame(unknown_data)
            st.dataframe(unknown_df, use_container_width=True)
            
            # Gráfico
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.barh(unknown_df['Columna'], unknown_df['Cantidad "unknown"'], color='orange', edgecolor='black')
            ax.set_xlabel('Cantidad de valores "unknown"')
            ax.set_title('Distribución de valores "unknown" por columna')
            st.pyplot(fig)
            
            st.markdown("**📝 Discusión:**")
            st.markdown("""
            - Los valores **`unknown`** **NO son errores**.
            - Representan que **el cliente no respondió** o la información **no estaba disponible**.
            - Se mantienen como **categoría separada** ("no sabe / no responde").
            """)
        else:
            st.success("✅ No hay valores 'unknown' en el dataset")
        
        st.markdown("---")
        
        # ========== 5. RESUMEN ==========
        st.markdown("### 📊 Resumen ejecutivo")
        
        total_unknown = sum([d['Cantidad "unknown"'] for d in unknown_data]) if unknown_data else 0
        columnas_unknown = len(unknown_data) if unknown_data else 0
        
        st.markdown(f"""
        | Indicador | Valor |
        |-----------|-------|
        | **Total de filas** | {len(df):,} |
        | **Total de columnas** | {len(df.columns)} |
        | **Variables numéricas** | {len(df.select_dtypes(include=[np.number]).columns)} |
        | **Variables categóricas** | {len(df.select_dtypes(include=['object']).columns)} |
        | **Valores 999 convertidos a NaN** | ~39,540 (~96% de `pdays`) |
        | **Valores 'unknown'** | {total_unknown} en {columnas_unknown} columnas |
        """)    

    # ==================== TAB 1: ÍTEM 2 ====================
    with tabs[1]:
        st.subheader("📌 Ítem 2: Clasificación de Variables")
        st.markdown("**Requisitos:** Identificar variables numéricas y categóricas, usar función personalizada, mostrar resultados con conteo")
        
        # ========== 1. FUNCIÓN PERSONALIZADA ==========
        st.markdown("### 🔧 1. Función personalizada para clasificar variables")
        
        def clasificar_variables(dataframe):
            numericas = []
            categoricas = []
            for columna in dataframe.columns:
                if pd.api.types.is_numeric_dtype(dataframe[columna]):
                    numericas.append(columna)
                else:
                    categoricas.append(columna)
            return numericas, categoricas
        
        num_cols, cat_cols = clasificar_variables(df)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("🔢 Variables Numéricas", len(num_cols))
            with st.expander("Ver lista completa"):
                st.write(num_cols)
        with col2:
            st.metric("🏷️ Variables Categóricas", len(cat_cols))
            with st.expander("Ver lista completa"):
                st.write(cat_cols)
        
        st.markdown("---")
        
        # ========== 2. CONTEO DE VARIABLES NUMÉRICAS ==========
        st.markdown("### 📊 2. Análisis de Variables Numéricas")
        st.markdown("Estadísticas básicas (media, min, max)")
        df_num = df[num_cols]
        st.dataframe(df_num.describe().round(2), use_container_width=True)
        
        st.markdown("---")
        
        # ========== 3. CONTEO DE VARIABLES CATEGÓRICAS ==========
        st.markdown("### 📊 3. Análisis de Variables Categóricas")
        st.markdown("Frecuencia de cada categoría usando `.value_counts()`")
        
        variables_categoricas_mostrar = [
            'job', 'marital', 'education', 'housing', 'loan', 
            'default', 'contact', 'month', 'day_of_week', 'poutcome'
        ]
        
        variables_existentes = [var for var in variables_categoricas_mostrar if var in cat_cols]
        
        # Crear subtabs para cada variable categórica
        sub_tabs = st.tabs(variables_existentes)
        
        for i, var in enumerate(variables_existentes):
            with sub_tabs[i]:
                st.markdown(f"### 📌 Variable: `{var}`")
                
                conteo = df[var].value_counts()
                conteo_df = pd.DataFrame({
                    'Categoría': conteo.index,
                    'Frecuencia': conteo.values,
                    'Porcentaje (%)': (conteo.values / len(df) * 100).round(2)
                })
                st.dataframe(conteo_df, use_container_width=True, hide_index=True)
                
                # Gráfico de barras
                fig, ax = plt.subplots(figsize=(10, 5))
                barras = ax.bar(range(len(conteo)), conteo.values, color='skyblue', edgecolor='black')
                ax.set_xticks(range(len(conteo)))
                ax.set_xticklabels(conteo.index, rotation=45, ha='right')
                ax.set_title(f'Distribución de {var}')
                ax.set_ylabel('Frecuencia')
                plt.tight_layout()
                st.pyplot(fig)
                
                categoria_top = conteo.index[0]
                porcentaje_top = (conteo.values[0] / len(df) * 100)
                st.info(f"💡 **Categoría más frecuente:** `{categoria_top}` con {conteo.values[0]:,} clientes ({porcentaje_top:.1f}%)")
        
        # ========== 4. VARIABLE OBJETIVO 'y' (AHORA FUERA DEL BUCLE) ==========
        st.markdown("---")
        st.markdown("### 🎯 4. Variable objetivo: `y` (aceptación de la campaña)")
        
        if 'y' in df.columns:
            conteo_y = df['y'].value_counts()
            
            col1_y, col2_y = st.columns(2)
            with col1_y:
                st.markdown("**Conteo:**")
                st.dataframe(conteo_y, use_container_width=True)
            
            with col2_y:
                fig_y, ax_y = plt.subplots(figsize=(6, 4))
                colores_y = ['#e74c3c', '#2ecc71']
                ax_y.pie(conteo_y.values, labels=conteo_y.index, autopct='%1.1f%%', colors=colores_y, startangle=90)
                ax_y.set_title('Proporción de aceptación')
                st.pyplot(fig_y)
            
            aceptacion = (df['y'] == 'yes').sum() / len(df) * 100
            st.info(f"📈 **Tasa de aceptación general:** {aceptacion:.2f}% de los clientes aceptaron la campaña")


            # ==================== TAB 2: ÍTEM 3 ====================
    with tabs[2]:
        st.subheader("📊 Ítem 3: Estadísticas Descriptivas")
        st.markdown("**Requisitos:** .describe(), media, mediana, moda, dispersión")
        
        # ========== 1. .describe() ==========
        st.markdown("### 📋 1. Resumen estadístico con .describe()")
        
        # Seleccionar solo columnas numéricas
        df_num = df.select_dtypes(include=[np.number])
        
        # Mostrar .describe()
        st.dataframe(df_num.describe().round(2), use_container_width=True)
        
        st.markdown("---")
        
        # ========== 2. MEDIA, MEDIANA Y DISPERSIÓN ==========
        st.markdown("### 📈 2. Interpretación: Media, Mediana y Dispersión")
        
        # Variable: age (edad)
        if 'age' in df_num.columns:
            st.markdown("#### 🟢 Variable: `age` (edad del cliente)")
            
            media_age = df_num['age'].mean()
            mediana_age = df_num['age'].median()
            std_age = df_num['age'].std()
            min_age = df_num['age'].min()
            max_age = df_num['age'].max()
            
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.metric("Media", f"{media_age:.1f}")
            with col2:
                st.metric("Mediana", f"{mediana_age:.1f}")
            with col3:
                st.metric("Desv. Estándar", f"{std_age:.1f}")
            with col4:
                st.metric("Mínimo", f"{min_age:.0f}")
            with col5:
                st.metric("Máximo", f"{max_age:.0f}")
            
            # Interpretación
            if abs(media_age - mediana_age) < 1:
                st.markdown(f"📌 **Interpretación:** Media ({media_age:.1f}) y mediana ({mediana_age:.1f}) son **prácticamente iguales**. La distribución de edades es **simétrica**.")
            elif media_age > mediana_age:
                st.markdown(f"📌 **Interpretación:** Media ({media_age:.1f}) > Mediana ({mediana_age:.1f}). La distribución tiene **cola hacia la derecha** (existen clientes de mayor edad que elevan el promedio).")
            else:
                st.markdown(f"📌 **Interpretación:** Media ({media_age:.1f}) < Mediana ({mediana_age:.1f}). La distribución tiene **cola hacia la izquierda**.")
            
            st.markdown(f"📌 **Dispersión:** La desviación estándar es de `{std_age:.1f}` años, lo que indica que las edades varían moderadamente alrededor de la media.")
        
        st.markdown("---")
        
        # Variable: duration (duración)
        if 'duration' in df_num.columns:
            st.markdown("#### 🟢 Variable: `duration` (duración del contacto en segundos)")
            
            media_dur = df_num['duration'].mean()
            mediana_dur = df_num['duration'].median()
            std_dur = df_num['duration'].std()
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Media", f"{media_dur:.0f} seg")
            with col2:
                st.metric("Mediana", f"{mediana_dur:.0f} seg")
            with col3:
                st.metric("Desv. Estándar", f"{std_dur:.0f} seg")
            
            st.markdown(f"📌 **Interpretación:** La duración media es de `{media_dur:.0f}` segundos, pero la desviación estándar es muy alta (`{std_dur:.0f}` segundos). Esto indica una **gran dispersión**: hay llamadas muy cortas (pocos segundos) y llamadas muy largas (miles de segundos).")
            
            if media_dur > mediana_dur:
                st.markdown(f"📌 La media ({media_dur:.0f}) es mayor que la mediana ({mediana_dur:.0f}), lo que confirma la existencia de **valores extremos** (llamadas muy largas) que elevan el promedio.")
        
        st.markdown("---")
        
        # Variable: campaign (número de contactos)
        if 'campaign' in df_num.columns:
            st.markdown("#### 🟢 Variable: `campaign` (número de contactos en esta campaña)")
            
            media_camp = df_num['campaign'].mean()
            mediana_camp = df_num['campaign'].median()
            std_camp = df_num['campaign'].std()
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Media", f"{media_camp:.2f}")
            with col2:
                st.metric("Mediana", f"{mediana_camp:.0f}")
            with col3:
                st.metric("Desv. Estándar", f"{std_camp:.2f}")
            
            st.markdown(f"📌 **Interpretación:** En promedio, los clientes reciben `{media_camp:.2f}` contactos. La mediana es `{mediana_camp:.0f}`, lo que significa que **la mayoría recibe pocos contactos**, pero algunos reciben muchos (valores atípicos).")
        
        st.markdown("---")
        
        # ========== 3. MODA (valor más frecuente) ==========
        st.markdown("### 📌 3. Moda (valor más frecuente)")
        
        col_moda1, col_moda2, col_moda3 = st.columns(3)
        
        with col_moda1:
            if 'age' in df_num.columns:
                moda_age = df_num['age'].mode().iloc[0]
                st.metric("Moda de edad", f"{moda_age:.0f} años")
                st.caption("(edad más común)")
        
        with col_moda2:
            if 'campaign' in df_num.columns:
                moda_camp = df_num['campaign'].mode().iloc[0]
                st.metric("Moda de contactos", f"{moda_camp:.0f}")
                st.caption("(número más frecuente)")
        
        with col_moda3:
            if 'duration' in df_num.columns:
                moda_dur = df_num['duration'].mode().iloc[0]
                st.metric("Moda de duración", f"{moda_dur:.0f} seg")
                st.caption("(duración más común)")
        
        st.markdown("---")
        
        # ========== 4. RESUMEN DE HALLAZGOS ==========
        st.markdown("### 💡 4. Hallazgos clave de estadísticas descriptivas")
        
        st.markdown("""
        | Hallazgo | Implicancia |
        |----------|-------------|
        | La edad media es ~40 años, con distribución simétrica | El perfil del cliente es adulto joven-maduro |
        | La duración del contacto tiene alta dispersión | Existen llamadas extremadamente largas que podrían estar relacionadas con la aceptación |
        | La mediana de contactos es 1 | La mayoría de los clientes recibe un solo contacto |
        | La moda de edad es ~30-35 años | Es el grupo de edad que más aparece en el dataset |
        """)
    # ==================== TAB 3: ÍTEM 4 ====================
    with tabs[3]:
        st.subheader("⚠️ Ítem 4: Análisis de Valores Faltantes")
        st.markdown("**Requisitos:** Conteo, visualización simple, discusión breve")
        
        # ========== 0. TRANSFORMAR 999 A NaN (SOLO PARA ESTE ÍTEM) ==========
        # Hacemos una copia para no modificar el original
        df_item4 = df.copy()
        
        # Convertir 999 a NaN en pdays
        if 'pdays' in df_item4.columns:
            df_item4['pdays'] = df_item4['pdays'].replace(999, np.nan)
        
        # ========== 1. CONTEO DE VALORES NULOS (NaN) ==========
        st.markdown("### 📊 1. Conteo de valores nulos (NaN)")
        
        # Calcular nulos por columna
        nulos_por_columna = df_item4.isnull().sum()
        nulos_porcentaje = (nulos_por_columna / len(df_item4) * 100).round(2)
        
        # Crear DataFrame solo con columnas que tienen nulos
        nulos_df = pd.DataFrame({
            'Columna': nulos_por_columna.index,
            'Cantidad de nulos': nulos_por_columna.values,
            '% de nulos': nulos_porcentaje.values
        })
        nulos_df = nulos_df[nulos_df['Cantidad de nulos'] > 0]
        
        if len(nulos_df) > 0:
            st.dataframe(nulos_df, use_container_width=True)
            
            # Mostrar total de nulos
            total_nulos = nulos_df['Cantidad de nulos'].sum()
            st.metric("📌 Total de valores nulos en el dataset", f"{total_nulos:,}")
            
            # Mostrar cuántos 999 había originalmente
            st.info(f"💡 **Nota:** Los {nulos_df[nulos_df['Columna'] == 'pdays']['Cantidad de nulos'].values[0]:,} valores nulos en `pdays` provienen de la conversión de `999` (que significaba 'no hay información en ese campo').")
        else:
            st.success("✅ No hay valores nulos (NaN) en el dataset")
        
        st.markdown("---")
        
        # ========== 2. VISUALIZACIÓN SIMPLE ==========
        st.markdown("### 📊 2. Visualización de valores faltantes")
        
        if len(nulos_df) > 0:
            # Gráfico de barras horizontales
            fig, ax = plt.subplots(figsize=(10, 5))
            colores = ['salmon' if col == 'pdays' else 'lightblue' for col in nulos_df['Columna']]
            ax.barh(nulos_df['Columna'], nulos_df['Cantidad de nulos'], color=colores, edgecolor='black')
            ax.set_xlabel('Cantidad de valores nulos')
            ax.set_title('Distribución de valores faltantes por columna')
            
            # Agregar etiquetas con los números
            for i, (col, val) in enumerate(zip(nulos_df['Columna'], nulos_df['Cantidad de nulos'])):
                ax.text(val + 100, i, f'{val:,}', va='center', fontsize=10)
            
            st.pyplot(fig)
        else:
            st.info("📊 No hay valores nulos para visualizar")
        
        st.markdown("---")
        
        # ========== 3. DISCUSIÓN BREVE ==========
        st.markdown("### 📝 3. Discusión breve sobre valores faltantes")
        
        # Verificar si pdays tiene nulos después de la conversión
        pdays_nulos = df_item4['pdays'].isna().sum() if 'pdays' in df_item4.columns else 0
        
        if pdays_nulos > 0:
            pdays_porcentaje = (pdays_nulos / len(df_item4) * 100).round(2)
            
            st.markdown(f"""
            **🔍 Análisis de valores nulos:**
            
            1. **`pdays` (días desde la última gestión)** es la **única columna con valores nulos** después de la transformación.
            
            2. **Cantidad:** {pdays_nulos:,} valores nulos ({pdays_porcentaje}% del total).
            
            3. **¿De dónde vienen estos nulos?** 
            - En el dataset original, el valor `999` significaba **"el cliente no cuenta con información"**.
            - **En este análisis, hemos convertido esos `999` a `NaN` (nulos)** para que no afecten cálculos estadísticos como la media.
        
             """)
        
        
        st.markdown("---")
        
        # ========== 4. VALORES "UNKNOWN" ==========
        st.markdown("### ❓ 4. Valores 'unknown' (información no proporcionada)")
        
        columnas_categoricas = df_item4.select_dtypes(include=['object']).columns.tolist()
        unknown_data = []
        
        for col in columnas_categoricas:
            count_unknown = (df_item4[col] == 'unknown').sum()
            if count_unknown > 0:
                unknown_data.append({
                    'Columna': col,
                    'Cantidad "unknown"': count_unknown,
                    '% "unknown"': round(count_unknown / len(df_item4) * 100, 2)
                })
        
        if unknown_data:
            unknown_df = pd.DataFrame(unknown_data)
            st.dataframe(unknown_df, use_container_width=True)
            
            fig2, ax2 = plt.subplots(figsize=(10, 5))
            ax2.barh(unknown_df['Columna'], unknown_df['Cantidad "unknown"'], color='orange', edgecolor='black')
            ax2.set_xlabel('Cantidad de valores "unknown"')
            ax2.set_title('Distribución de valores "unknown" por columna')
            
            for i, (col, val) in enumerate(zip(unknown_df['Columna'], unknown_df['Cantidad "unknown"'])):
                ax2.text(val + 50, i, f'{val:,}', va='center', fontsize=10)
            
            st.pyplot(fig2)
            
            st.markdown("""
            **📝 Discusión sobre 'unknown':**
            
            - Significan que **el cliente no proporcionó esa información**.
             """)
        else:
            st.success("✅ No hay valores 'unknown' en el dataset")
        
        st.markdown("---")
        
        # ========== 5. RESUMEN ==========
        st.markdown("### 📊 5. Resumen ejecutivo")
        
        total_unknown = sum([d['Cantidad "unknown"'] for d in unknown_data]) if unknown_data else 0
        
        st.markdown(f"""
        | Tipo de dato faltante | Columnas afectadas | Cantidad total |
        |----------------------|-------------------|----------------|
        | **NaN (nulos)** | `pdays` | {pdays_nulos:,} |
        | **'unknown'** | {', '.join([d['Columna'] for d in unknown_data]) if unknown_data else 'ninguna'} | {total_unknown} |
        """)
        
    # ==================== TAB 4: ÍTEM 5 ====================
    with tabs[4]:
        st.subheader("📈 Ítem 5: Distribución de Variables Numéricas")
        st.markdown("**Requisitos:** Histogramas, uso de Matplotlib/Seaborn, interpretación visual")
        st.markdown("A continuación se muestran **TODAS** las variables numéricas del dataset.")
        
        # ========== 1. OBTENER VARIABLES NUMÉRICAS ==========
        columnas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
        
        # Excluir pdays por los nulos
        if 'pdays' in columnas_numericas:
            columnas_numericas.remove('pdays')
        
        # Nombres amigables
        nombres_amigables = {
            'age': 'Edad (años)',
            'duration': 'Duración del contacto (segundos)',
            'campaign': 'Número de contactos en esta campaña',
            'previous': 'Contactos en campañas anteriores',
            'emp.var.rate': 'Variación del empleo (%)',
            'cons.price.idx': 'Índice de precios al consumidor (IPC)',
            'cons.conf.idx': 'Índice de confianza del consumidor',
            'euribor3m': 'Tasa de interés Euribor (3 meses)',
            'nr.employed': 'Número de empleados'
        }
        
        # Mostrar cada variable numérica
        for i, var in enumerate(columnas_numericas):
            nombre_mostrar = nombres_amigables.get(var, var)
            
            st.markdown(f"---")
            st.markdown(f"### 📊 Variable {i+1}: `{var}` - {nombre_mostrar}")
            
            # Crear dos columnas: histograma y boxplot
            col_hist, col_box = st.columns(2)
            
            # ----- HISTOGRAMA -----
            with col_hist:
                st.markdown("**Histograma (distribución de frecuencias)**")
                
                fig_hist, ax_hist = plt.subplots(figsize=(8, 5))
                ax_hist.hist(df[var].dropna(), bins=30, edgecolor='black', 
                            alpha=0.7, color='steelblue')
                ax_hist.set_title(f'Distribución de {nombre_mostrar}', fontsize=12)
                ax_hist.set_xlabel(nombre_mostrar, fontsize=10)
                ax_hist.set_ylabel('Frecuencia (cantidad de clientes)', fontsize=10)
                ax_hist.grid(True, alpha=0.3)
                
                st.pyplot(fig_hist)
            
            # ----- BOXPLOT -----
            with col_box:
                st.markdown("**Boxplot (dispersión y valores atípicos)**")
                
                fig_box, ax_box = plt.subplots(figsize=(8, 5))
                ax_box.boxplot(df[var].dropna(), vert=True, patch_artist=True,
                            boxprops=dict(facecolor='lightgreen', color='black'),
                            whiskerprops=dict(color='black'),
                            capprops=dict(color='black'),
                            medianprops=dict(color='red', linewidth=2))
                ax_box.set_title(f'Boxplot de {nombre_mostrar}', fontsize=12)
                ax_box.set_ylabel(nombre_mostrar, fontsize=10)
                ax_box.set_xticklabels([nombre_mostrar])
                ax_box.grid(True, alpha=0.3, axis='y')
                
                st.pyplot(fig_box)
            
            # ----- INTERPRETACIÓN -----
            st.markdown("**📝 Interpretación visual:**")
            
            # Calcular estadísticas
            data_clean = df[var].dropna()
            media = data_clean.mean()
            mediana = data_clean.median()
            std = data_clean.std()
            skewness = data_clean.skew()
            min_val = data_clean.min()
            max_val = data_clean.max()
            
            # Mostrar estadísticas
            col_stats1, col_stats2, col_stats3, col_stats4 = st.columns(4)
            with col_stats1:
                st.metric("Media", f"{media:.2f}")
            with col_stats2:
                st.metric("Mediana", f"{mediana:.2f}")
            with col_stats3:
                st.metric("Desv. Estándar", f"{std:.2f}")
            with col_stats4:
                st.metric("Asimetría", f"{skewness:.2f}")
            
            # Análisis de la distribución
            st.markdown("**🔍 Análisis de la distribución:**")
            
            if abs(skewness) < 0.5:
                st.markdown(f"- 📊 Distribución **aproximadamente simétrica** (asimetría = {skewness:.2f}).")
            elif skewness > 0:
                st.markdown(f"- 📊 Distribución con **cola a la derecha** (asimetría positiva = {skewness:.2f}).")
                st.markdown(f"  - Hay **valores extremadamente altos** que elevan la media.")
                st.markdown(f"  - Media ({media:.2f}) > Mediana ({mediana:.2f})")
            else:
                st.markdown(f"- 📊 Distribución con **cola a la izquierda** (asimetría negativa = {skewness:.2f}).")
                st.markdown(f"  - Hay **valores extremadamente bajos** que tiran la media hacia abajo.")
                st.markdown(f"  - Media ({media:.2f}) < Mediana ({mediana:.2f})")
            
            # Dispersión
            if std > media * 0.5:
                st.markdown(f"- 📊 **Alta dispersión:** Los datos varían mucho (std = {std:.2f}).")
            else:
                st.markdown(f"- 📊 **Baja dispersión:** La mayoría de los datos están cerca de la media.")
            
            # Valores atípicos
            if max_val > media + 2*std:
                st.markdown(f"- ⚠️ **Valores atípicos detectados:** Máximo = {max_val:.0f} (muy por encima de la media).")
            
            st.markdown("---")
        
        # ========== NOTA SOBRE PDAYS ==========
        st.info("💡 **Nota:** La variable `pdays` tiene 96% de valores nulos (clientes sin campaña anterior). Por eso no se incluye en este análisis, ya que su distribución estaría sesgada.")
        
        # ==================== TAB 5: ÍTEM 6 ====================
    with tabs[5]:
        st.subheader("📊 Ítem 6: Análisis de Variables Categóricas")
        st.markdown("**Requisitos:** Conteos, gráficos de barras, proporciones")
        st.markdown("A continuación se muestran **TODAS** las variables categóricas del dataset.")
        
        # Obtener todas las columnas categóricas (excluyendo 'y' que va al final)
        columnas_categoricas = df.select_dtypes(include=['object']).columns.tolist()
        if 'y' in columnas_categoricas:
            columnas_categoricas.remove('y')
        
        # Mostrar cada variable categórica
        for i, var in enumerate(columnas_categoricas):
            st.markdown(f"---")
            st.markdown(f"### 📌 Variable {i+1}: `{var}`")
            
            # Calcular conteos
            conteo = df[var].value_counts()
            porcentajes = (conteo / len(df) * 100).round(2)
            
            # Tabla de conteos
            resultados_df = pd.DataFrame({
                'Categoría': conteo.index,
                'Frecuencia': conteo.values,
                'Porcentaje (%)': porcentajes.values
            })
            st.dataframe(resultados_df, use_container_width=True, hide_index=True)
            
            # Gráfico de barras
            fig_bar, ax_bar = plt.subplots(figsize=(10, 5))
            barras = ax_bar.bar(range(len(conteo)), conteo.values, color='skyblue', edgecolor='black')
            ax_bar.set_xticks(range(len(conteo)))
            ax_bar.set_xticklabels(conteo.index, rotation=45, ha='right')
            ax_bar.set_title(f'Distribución de {var}')
            ax_bar.set_ylabel('Frecuencia')
            
            for j, bar in enumerate(barras):
                ax_bar.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
                        f'{conteo.values[j]:,}', ha='center', fontsize=9)
            
            plt.tight_layout()
            st.pyplot(fig_bar)
            
            # Gráfico de pastel (proporciones)
            fig_pie, ax_pie = plt.subplots(figsize=(6, 6))
            colores_pie = plt.cm.Set3(range(len(conteo)))
            ax_pie.pie(conteo.values, labels=conteo.index, autopct='%1.1f%%',
                    colors=colores_pie, startangle=90)
            ax_pie.set_title(f'Proporciones de {var}')
            st.pyplot(fig_pie)
            
            # Interpretación breve
            categoria_top = conteo.index[0]
            st.info(f"💡 **Categoría más común:** `{categoria_top}` con {conteo.values[0]:,} clientes ({porcentajes.iloc[0]:.1f}%)")
        
        # Variable objetivo 'y' al final
        st.markdown(f"---")
        st.markdown(f"### 🎯 Variable objetivo: `y`")
        
        conteo_y = df['y'].value_counts()
        porcentajes_y = (conteo_y / len(df) * 100).round(2)
        
        resultados_y = pd.DataFrame({
            'Categoría': conteo_y.index,
            'Frecuencia': conteo_y.values,
            'Porcentaje (%)': porcentajes_y.values
        })
        st.dataframe(resultados_y, use_container_width=True, hide_index=True)
        
        fig_y_bar, ax_y_bar = plt.subplots(figsize=(8, 5))
        colores_y = ['#e74c3c', '#2ecc71']
        barras_y = ax_y_bar.bar(conteo_y.index, conteo_y.values, color=colores_y, edgecolor='black')
        ax_y_bar.set_title('Distribución de la variable objetivo (y)')
        ax_y_bar.set_ylabel('Cantidad de clientes')
        
        for j, bar in enumerate(barras_y):
            ax_y_bar.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 100,
                        f'{conteo_y.values[j]:,}', ha='center', fontsize=10)
        
        st.pyplot(fig_y_bar)
        
        aceptacion = (df['y'] == 'yes').sum()
        aceptacion_pct = (aceptacion / len(df) * 100).round(2)
        st.info(f"💡 **Tasa de aceptación general:** {aceptacion_pct}% de los clientes aceptaron la campaña")
            

    # ==================== TAB 6: ÍTEM 7 ====================
    with tabs[6]:
        st.subheader("🔗 Ítem 7: Análisis Bivariado (Numérico vs Categórico)")
        st.markdown("**Requisitos:** age vs y, duration vs y")
        st.markdown("A continuación se muestran **TODAS** las variables numéricas comparadas con la aceptación (`y`).")
        
        # Obtener todas las columnas numéricas
        columnas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
        
        # Excluir pdays por los nulos
        if 'pdays' in columnas_numericas:
            columnas_numericas.remove('pdays')
        
        # Nombres amigables
        nombres_amigables = {
            'age': 'Edad (años)',
            'duration': 'Duración del contacto (segundos)',
            'campaign': 'Número de contactos en esta campaña',
            'previous': 'Contactos en campañas anteriores',
            'emp.var.rate': 'Variación del empleo (%)',
            'cons.price.idx': 'Índice de precios al consumidor (IPC)',
            'cons.conf.idx': 'Índice de confianza del consumidor',
            'euribor3m': 'Tasa de interés Euribor (3 meses)',
            'nr.employed': 'Número de empleados'
        }
        
        # Mostrar cada variable numérica
        for i, var in enumerate(columnas_numericas):
            st.markdown(f"---")
            nombre_mostrar = nombres_amigables.get(var, var)
            st.markdown(f"### 📌 Variable {i+1}: `{var}` - {nombre_mostrar}")
            
            # Calcular medias por grupo
            media_yes = df[df['y'] == 'yes'][var].mean()
            media_no = df[df['y'] == 'no'][var].mean()
            
            # Gráfico de barras
            fig, ax = plt.subplots(figsize=(8, 5))
            categorias = ['No aceptaron (no)', 'Aceptaron (yes)']
            valores = [media_no, media_yes]
            colores = ['#e74c3c', '#2ecc71']
            
            barras = ax.bar(categorias, valores, color=colores, edgecolor='black', width=0.5)
            ax.set_title(f'{nombre_mostrar} según aceptación de la campaña', fontsize=14)
            ax.set_ylabel(nombre_mostrar, fontsize=12)
            
            # Agregar etiquetas
            for j, (bar, val) in enumerate(zip(barras, valores)):
                ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + (max(valores)*0.02), 
                    f'{val:.2f}', ha='center', fontweight='bold', fontsize=11)
            
            st.pyplot(fig)
            
            # Interpretación
            diferencia = media_yes - media_no
            if diferencia > 0:
                st.success(f"✅ **Conclusión:** Los clientes que aceptaron tienen **{diferencia:.2f} unidades MÁS** en `{var}`")
            elif diferencia < 0:
                st.success(f"✅ **Conclusión:** Los clientes que aceptaron tienen **{abs(diferencia):.2f} unidades MENOS** en `{var}`")
            else:
                st.info(f"ℹ️ **Conclusión:** No hay diferencia significativa en `{var}`")
            
            # Estadísticas detalladas
            with st.expander(f"📊 Ver estadísticas detalladas de {var}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**✅ Aceptaron (yes)**")
                    st.markdown(f"- Media: {media_yes:.2f}")
                    st.markdown(f"- Mediana: {df[df['y'] == 'yes'][var].median():.2f}")
                    st.markdown(f"- Desv. Estándar: {df[df['y'] == 'yes'][var].std():.2f}")
                with col2:
                    st.markdown("**❌ No aceptaron (no)**")
                    st.markdown(f"- Media: {media_no:.2f}")
                    st.markdown(f"- Mediana: {df[df['y'] == 'no'][var].median():.2f}")
                    st.markdown(f"- Desv. Estándar: {df[df['y'] == 'no'][var].std():.2f}")


                    # ==================== TAB 7: ÍTEM 8 ====================
    with tabs[7]:
        st.subheader("🔗 Ítem 8: Análisis Bivariado (Categórico vs Categórico)")
        st.markdown("**Requisitos:** education vs y, contact vs y")
        st.markdown("A continuación se muestran **TODAS** las variables categóricas comparadas con la aceptación (`y`).")
        
        # Obtener todas las columnas categóricas (excluyendo 'y' que es la comparación)
        columnas_categoricas = df.select_dtypes(include=['object']).columns.tolist()
        if 'y' in columnas_categoricas:
            columnas_categoricas.remove('y')
        
        # Mostrar cada variable categórica vs y
        for i, var in enumerate(columnas_categoricas):
            st.markdown(f"---")
            st.markdown(f"### 📌 Variable {i+1}: `{var}` vs `y`")
            
            # Crear tabla de contingencia
            contingency = pd.crosstab(df[var], df['y'])
            
            # Calcular porcentajes por fila (tasa de aceptación por categoría)
            tasa_aceptacion = (contingency['yes'] / contingency.sum(axis=1) * 100).round(2)
            
            # Mostrar tabla
            st.markdown("**📊 Tabla de contingencia:**")
            st.dataframe(contingency, use_container_width=True)
            
            # Gráfico de barras agrupadas
            fig_bar, ax_bar = plt.subplots(figsize=(12, 6))
            contingency.plot(kind='bar', ax=ax_bar, edgecolor='black', color=['#e74c3c', '#2ecc71'])
            ax_bar.set_title(f'Relación entre {var} y aceptación de la campaña', fontsize=14)
            ax_bar.set_xlabel(var, fontsize=12)
            ax_bar.set_ylabel('Cantidad de clientes', fontsize=12)
            ax_bar.legend(title='Aceptación', labels=['No (no)', 'Sí (yes)'])
            ax_bar.tick_params(axis='x', rotation=45)
            
            # Agregar etiquetas con los valores
            for j, p in enumerate(ax_bar.patches):
                ax_bar.annotate(f'{int(p.get_height())}', 
                            (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha='center', va='center', xytext=(0, 5), textcoords='offset points', fontsize=8)
            
            plt.tight_layout()
            st.pyplot(fig_bar)
            
            # Gráfico de tasa de aceptación por categoría
            fig_tasa, ax_tasa = plt.subplots(figsize=(10, 5))
            colores_tasa = ['#2ecc71' if tasa > 10 else '#f39c12' if tasa > 5 else '#e74c3c' for tasa in tasa_aceptacion]
            barras_tasa = ax_tasa.bar(range(len(tasa_aceptacion)), tasa_aceptacion.values, color=colores_tasa, edgecolor='black')
            ax_tasa.set_xticks(range(len(tasa_aceptacion)))
            ax_tasa.set_xticklabels(tasa_aceptacion.index, rotation=45, ha='right')
            ax_tasa.set_title(f'Tasa de aceptación por {var}', fontsize=14)
            ax_tasa.set_ylabel('Tasa de aceptación (%)', fontsize=12)
            ax_tasa.set_xlabel(var, fontsize=12)
            
            for j, (bar, tasa) in enumerate(zip(barras_tasa, tasa_aceptacion.values)):
                ax_tasa.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                            f'{tasa}%', ha='center', fontsize=9)
            
            plt.tight_layout()
            st.pyplot(fig_tasa)
            
            # Interpretación
            mejor_categoria = tasa_aceptacion.idxmax()
            peor_categoria = tasa_aceptacion.idxmin()
            mejor_tasa = tasa_aceptacion.max()
            peor_tasa = tasa_aceptacion.min()
            
            st.markdown(f"""
            **📝 Interpretación:**
            
            - ✅ **Categoría con mayor aceptación:** `{mejor_categoria}` con **{mejor_tasa}%** de aceptación
            - ❌ **Categoría con menor aceptación:** `{peor_categoria}` con **{peor_tasa}%** de aceptación
            - 📊 **Diferencia:** {mejor_tasa - peor_tasa:.1f} puntos porcentuales entre la mejor y peor categoría
            """)
            
            # Mostrar 'unknown' si existe
            if 'unknown' in tasa_aceptacion.index:
                st.warning(f"⚠️ **Nota:** La categoría 'unknown' tiene una tasa de aceptación del {tasa_aceptacion['unknown']}%")   


    # ==================== TAB 8: ÍTEM 9 ====================
    with tabs[8]:
        st.subheader("🎛️ Ítem 9: Análisis Dinámico con Widgets")
        st.markdown("**Requisitos:** selectbox, multiselect, slider, checkbox")
        st.markdown("A continuación puede explorar los datos usando los controles interactivos.")
        
        st.markdown("---")
        
        # ========== SELECTOR 1: SLIDER (filtro de edad) ==========
        st.markdown("### 1. 📅 Filtro por edad (slider)")
        
        if 'age' in df.columns:
            edad_min = int(df['age'].min())
            edad_max = int(df['age'].max())
            
            rango_edad = st.slider(
                "Seleccione el rango de edad:",
                min_value=edad_min,
                max_value=edad_max,
                value=(edad_min, edad_max)
            )
            
            # Aplicar filtro
            df_filtrado = df[(df['age'] >= rango_edad[0]) & (df['age'] <= rango_edad[1])]
            st.write(f"✅ **Clientes en este rango:** {len(df_filtrado):,} de {len(df):,} total")
        else:
            df_filtrado = df
        
        st.markdown("---")
        
        # ========== SELECTOR 2: SELECTBOX (elegir variable) ==========
        st.markdown("### 2. 📊 Variable a analizar (selectbox)")
        
        # Opciones para el selectbox
        opciones_select = ['age', 'duration', 'campaign', 'previous', 'y']
        opciones_existentes = [op for op in opciones_select if op in df.columns]
        
        variable_seleccionada = st.selectbox(
            "Elija una variable para ver su análisis:",
            opciones_existentes
        )
        
        # Mostrar análisis de la variable seleccionada
        if variable_seleccionada == 'y':
            conteo = df_filtrado['y'].value_counts()
            st.write("**Distribución de aceptación:**")
            st.write(f"- ✅ Aceptaron (yes): {conteo.get('yes', 0):,} clientes")
            st.write(f"- ❌ No aceptaron (no): {conteo.get('no', 0):,} clientes")
            
            aceptacion_pct = (conteo.get('yes', 0) / len(df_filtrado) * 100) if len(df_filtrado) > 0 else 0
            st.metric("Tasa de aceptación", f"{aceptacion_pct:.2f}%")
            
        elif variable_seleccionada in df_filtrado.columns:
            if pd.api.types.is_numeric_dtype(df_filtrado[variable_seleccionada]):
                st.write(f"**Estadísticas de {variable_seleccionada}:**")
                st.write(f"- Media: {df_filtrado[variable_seleccionada].mean():.2f}")
                st.write(f"- Mediana: {df_filtrado[variable_seleccionada].median():.2f}")
                st.write(f"- Mínimo: {df_filtrado[variable_seleccionada].min():.2f}")
                st.write(f"- Máximo: {df_filtrado[variable_seleccionada].max():.2f}")
            else:
                conteo = df_filtrado[variable_seleccionada].value_counts()
                st.dataframe(conteo, use_container_width=True)
        
        st.markdown("---")
        
        # ========== SELECTOR 3: MULTISELECT (elegir columnas) ==========
        st.markdown("### 3. 📋 Columnas para visualizar (multiselect)")
        
        columnas_default = ['age', 'job', 'education', 'y']
        columnas_default_existentes = [col for col in columnas_default if col in df.columns]
        
        columnas_elegidas = st.multiselect(
            "Seleccione las columnas que quiere ver en la tabla:",
            options=df.columns.tolist(),
            default=columnas_default_existentes
        )
        
        if columnas_elegidas:
            st.dataframe(df_filtrado[columnas_elegidas].head(10), use_container_width=True)
            st.caption(f"Mostrando 10 filas de {len(df_filtrado):,} clientes")
        else:
            st.info("Seleccione al menos una columna")
        
        st.markdown("---")
        
        # ========== SELECTOR 4: CHECKBOX (mostrar estadísticas) ==========
        st.markdown("### 4. 📈 Estadísticas adicionales (checkbox)")
        
        mostrar_stats = st.checkbox("Mostrar estadísticas del filtro actual")
        
        if mostrar_stats:
            st.markdown("**📊 Resumen de los datos filtrados:**")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total de clientes", f"{len(df_filtrado):,}")
            with col2:
                st.metric("Edad promedio", f"{df_filtrado['age'].mean():.1f}" if 'age' in df_filtrado.columns else "N/A")
            with col3:
                if 'y' in df_filtrado.columns:
                    aceptacion = (df_filtrado['y'] == 'yes').sum()
                    st.metric("Aceptaron campaña", f"{aceptacion:,}")
            
            st.markdown("**Variables numéricas (estadísticas):**")
            df_num = df_filtrado.select_dtypes(include=[np.number])
            if len(df_num.columns) > 0:
                st.dataframe(df_num.describe().round(2), use_container_width=True)
        
        st.markdown("---")
        st.info("💡 **Resumen:** Use los controles para filtrar y explorar los datos. El slider cambia el rango de edad, el selectbox elige una variable, el multiselect elige columnas y el checkbox muestra estadísticas.")


            # ==================== TAB 9: ÍTEM 10 ====================
    with tabs[9]:
        st.subheader("💡 Ítem 10: Hallazgos Clave del EDA")
        st.markdown("**Requisitos:** Visualización resumen, insights principales derivados del EDA")
        
        # ========== 1. GRÁFICO RESUMEN DE LA VARIABLE OBJETIVO ==========
        st.markdown("### 📊 1. Resumen de la variable objetivo (y)")
        
        if 'y' in df.columns:
            conteo_y = df['y'].value_counts()
            aceptacion_pct = (conteo_y.get('yes', 0) / len(df) * 100)
            
            fig1, ax1 = plt.subplots(figsize=(8, 5))
            colores_y = ['#e74c3c', '#2ecc71']
            barras = ax1.bar(conteo_y.index, conteo_y.values, color=colores_y, edgecolor='black')
            ax1.set_title('Distribución de la variable objetivo (y)', fontsize=14)
            ax1.set_ylabel('Cantidad de clientes', fontsize=12)
            
            for bar, val in zip(barras, conteo_y.values):
                ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 200, 
                        f'{val:,}', ha='center', fontweight='bold')
            
            st.pyplot(fig1)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("✅ Aceptaron (yes)", f"{conteo_y.get('yes', 0):,}")
            with col2:
                st.metric("❌ No aceptaron (no)", f"{conteo_y.get('no', 0):,}")
            with col3:
                st.metric("📊 Tasa de aceptación", f"{aceptacion_pct:.1f}%")
        
        st.markdown("---")
        
        # ========== 2. TOP 5 HALLAZGOS MÁS IMPORTANTES ==========
        st.markdown("### 🔍 2. Top 5 Hallazgos Más Importantes")
        
        # Hallazgo 1: Duration
        st.markdown("""
        **1️⃣ La duración del contacto es el factor MÁS determinante**
        
        | Grupo | Duración promedio |
        |-------|-------------------|
        | Aceptaron (yes) | **553 segundos** |
        | No aceptaron (no) | **221 segundos** |
        
        > 📌 **Conclusión:** Las llamadas exitosas duran en promedio **2.5 VECES MÁS** que las no exitosas.
        > 💡 **Recomendación:** Invertir tiempo en llamadas más largas y personalizadas.
        """)
        
        # Hallazgo 2: Campaign
        st.markdown("""
        **2️⃣ Menos contactos = mayor probabilidad de éxito**
        
        | Grupo | Contactos promedio |
        |-------|-------------------|
        | Aceptaron (yes) | **2.05 contactos** |
        | No aceptaron (no) | **2.63 contactos** |
        
        > 📌 **Conclusión:** Los clientes que aceptaron recibieron **MENOS contactos**.
        > 💡 **Recomendación:** Evitar bombardear a los clientes; calidad sobre cantidad.
        """)
        
        # Hallazgo 3: Poutcome
        st.markdown("""
        **3️⃣ El éxito en campañas anteriores predice éxito actual**
        
        | Resultado anterior | Aceptaron |
        |--------------------|-----------|
        | success | **894 clientes** |
        | failure | **605 clientes** |
        | nonexistent | **3,141 clientes** |
        
        > 📌 **Conclusión:** Los clientes que aceptaron en el pasado tienen ALTA probabilidad de aceptar nuevamente.
        > 💡 **Recomendación:** Priorizar en futuras campañas a clientes con historial de éxito.
        """)
        
        # Hallazgo 4: Job
        st.markdown("""
        **4️⃣ El tipo de trabajo influye significativamente**
        
        | Trabajo | Aceptaron | Tasa aprox. |
        |---------|-----------|-------------|
        | student | 327 | **84%** |
        | retired | 434 | **25%** |
        | unemployed | 293 | **17%** |
        | admin. | 1,352 | **13%** |
        
        > 📌 **Conclusión:** **Estudiantes y jubilados** tienen la más alta tasa de aceptación.
        > 💡 **Recomendación:** Enfocar campañas en estos segmentos.
        """)
        
        # Hallazgo 5: Education
        st.markdown("""
        **5️⃣ La educación universitaria se asocia con mayor aceptación**
        
        | Nivel educativo | Aceptaron |
        |-----------------|-----------|
        | university.degree | **595** |
        | high.school | **484** |
        | professional.course | **251** |
        
        > 📌 **Conclusión:** Los clientes con **educación universitaria** tienen mayor tasa de aceptación.
        > 💡 **Recomendación:** Personalizar mensajes según nivel educativo.
        """)
        
        st.markdown("---")
        
        # ========== 3. OTROS HALLAZGOS RELEVANTES ==========
        st.markdown("### 📌 3. Otros Hallazgos Relevantes")
        
        col_otros1, col_otros2 = st.columns(2)
        
        with col_otros1:
            st.markdown("""
            **📊 Edad (age)**
            - Aceptaron: **40.9 años**
            - No aceptaron: **39.9 años**
            - Diferencia: +1 año
            
            > Los clientes que aceptan son **ligeramente mayores**.
            """)
            
            st.markdown("""
            **📊 Contacto (contact)**
            - `telephone`: **787 aceptaron** / 3,853 no
            - `cellular`: **3,853 aceptaron** / 22,291 no
            
            > El canal **telefónico** tiene mejor **proporción** de éxito.
            """)
        
        with col_otros2:
            st.markdown("""
            **📊 Euribor (euribor3m)**
            - Aceptaron: **2.12**
            - No aceptaron: **3.81**
            
            > Tasas de interés **más bajas** se asocian con mayor aceptación.
            """)
            
            st.markdown("""
            **📊 Mes (month)**
            - Mayor aceptación: **mayo (3,886)**, **julio (3,655)**, **septiembre (3,142)**
            
            > Hay **estacionalidad** en la respuesta a la campaña.
            """)
        
        st.markdown("---")
        
       
# ======================================================================
# MÓDULO 4: CONCLUSIONES FINALES
# ======================================================================

elif pagina == "📝 Conclusiones":
    st.header("📝 Conclusiones del Análisis")
    st.markdown("Basado en el análisis exploratorio de datos (EDA) realizado al dataset BankMarketing.csv")
    st.markdown("---")
    
    # ========== 1. RESUMEN DE LA VARIABLE OBJETIVO ==========
    if st.session_state.datos_cargados:
        df = st.session_state.df
        
        st.subheader("📊 Resumen de la campaña")
        
        if 'y' in df.columns:
            total_clientes = len(df)
            aceptaron = (df['y'] == 'yes').sum()
            no_aceptaron = (df['y'] == 'no').sum()
            tasa = (aceptaron / total_clientes * 100)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("📊 Total clientes", f"{total_clientes:,}")
            with col2:
                st.metric("✅ Aceptaron", f"{aceptaron:,}")
            with col3:
                st.metric("📈 Tasa de aceptación", f"{tasa:.2f}%")
            
            # Gráfico simple
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.bar(['No aceptaron', 'Aceptaron'], [no_aceptaron, aceptaron], 
                   color=['#e74c3c', '#2ecc71'], edgecolor='black')
            ax.set_title('Resultado de la campaña')
            ax.set_ylabel('Cantidad de clientes')
            
            for i, v in enumerate([no_aceptaron, aceptaron]):
                ax.text(i, v + 200, f'{v:,}', ha='center', fontweight='bold')
            
            st.pyplot(fig)
        
        st.markdown("---")
        
        # ========== 2. LAS 5 CONCLUSIONES ==========
        st.subheader("🎯 5 Conclusiones Clave para la Toma de Decisiones")
        
        st.markdown("""
        **Conclusión 1: LA DURACIÓN DEL CONTACTO ES EL FACTOR DETERMINANTE**
        
        > Los clientes que aceptaron tuvieron llamadas de **553 segundos** en promedio,
        > mientras que los que no aceptaron solo **221 segundos**. Diferencia de **+332 segundos**.
        > 
        > ✅ **Acción recomendada:** Capacitar al equipo comercial para mantener llamadas más prolongadas y personalizadas.
        
        ---
        
        **Conclusión 2: ESTUDIANTES Y JUBILADOS SON EL PÚBLICO MÁS RECEPTIVO**
        
        > De 387 estudiantes, **327 aceptaron (84.5%)**. 
        > De 1,720 jubilados, **434 aceptaron (25.2%)**.
        > 
        > ✅ **Acción recomendada:** Segmentar las campañas priorizando estudiantes y jubilados.
        
        ---
        
        **Conclusión 3: HAY ESTACIONALIDAD EN LA RESPUESTA (MESES CLAVE)**
        
        > Los meses con MAYOR número de aceptaciones fueron:
        > - **Mayo:** 3,886 aceptaciones
        > - **Julio:** 3,655 aceptaciones  
        > - **Septiembre:** 3,142 aceptaciones
        > 
        > ⚠️ **Atención:** Agosto registró **CERO aceptaciones**.
        > 
        > ✅ **Acción recomendada:** Concentrar las campañas en mayo, julio y septiembre. Evitar agosto.
        
        ---
        
        **Conclusión 4: CLIENTES CON ÉXITO PREVIO VUELVEN A ACEPTAR**
        
        > Clientes con `poutcome=success`: **894 aceptaron vs 479 no aceptaron (65% de éxito)**.
        > 
        > ✅ **Acción recomendada:** Crear un programa de fidelización para clientes recurrentes.
        
        ---
        
        **Conclusión 5: MENOS CONTACTOS = MÁS PROBABILIDAD DE ÉXITO**
        
        > Aceptaron: **2.05 contactos** | No aceptaron: **2.63 contactos**.
        > 
        > ✅ **Acción recomendada:** Limitar a máximo 2 contactos por cliente para evitar saturación.
        """)
        
        st.markdown("---")
        
        # ========== 3. VISUALIZACIÓN RESUMEN ==========
        st.subheader("📊 Visualización Resumen: Factores que más influyen")
        
        # Datos resumen
        factores = ['Duración (seg)', 'Edad (años)', 'Contactos', 'Euribor']
        diferencia = [553 - 221, 40.9 - 39.9, 2.63 - 2.05, 3.81 - 2.12]
        
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        colores_factores = ['#2ecc71', '#3498db', '#e74c3c', '#f39c12']
        barras2 = ax2.barh(factores, diferencia, color=colores_factores, edgecolor='black')
        ax2.set_title('Diferencia entre grupos (Aceptaron vs No aceptaron)', fontsize=14)
        ax2.set_xlabel('Diferencia absoluta', fontsize=12)
        
        for bar, diff in zip(barras2, diferencia):
            ax2.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, 
                    f'{diff:.1f}', va='center', fontweight='bold')
        
        st.pyplot(fig2)
        
        st.caption("""
        **Interpretación del gráfico:**
        - **Duración:** +332 segundos (llamadas más largas)
        - **Edad:** +1 año (clientes ligeramente mayores)
        - **Contactos:** -0.58 contactos (menos saturación)
        - **Euribor:** -1.69 puntos (tasas más bajas)
        """)
        
        st.markdown("---")
        
        # ========== 4. RESUMEN EJECUTIVO FINAL ==========
        st.success("""
        ### 💡 Resumen Ejecutivo
        
        **La duración del contacto es el factor más importante.** 
        
        Para mejorar la tasa de aceptación de la campaña, se recomienda:
        
        1. 📞 **Llamadas más largas** (capacitar al equipo comercial)
        2. 🎯 **Segmentar por estudiantes y jubilados** (mayor tasa de respuesta)
        3. 📅 **Concentrar campañas en mayo, julio y septiembre** (evitar agosto)
        4. 🔁 **Aprovechar clientes con historial de éxito** (programa de fidelización)
        5. 📉 **Limitar contactos a máximo 2 por cliente** (evitar saturación)
        """)
        
    else:
        st.warning("⚠️ Primero debe cargar el dataset en el módulo 'Carga de Datos' para ver las conclusiones basadas en sus datos.")       