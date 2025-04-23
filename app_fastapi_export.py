
from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
from typing import Optional
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

app = FastAPI()

@app.get("/buscar_ensayos")
def buscar_ensayos(molecula: Optional[str] = None, patologia: Optional[str] = None, estado: Optional[str] = None, fase: Optional[str] = None, pais: Optional[str] = None, formato: Optional[str] = None):
    return {"mensaje": "Búsqueda simulada", "molecula": molecula, "patologia": patologia}

@app.get("/ensayo_detalle")
def ensayo_detalle(id: str):
    return {"id": id, "detalle": "Información detallada del ensayo clínico"}

@app.get("/criterios_ensayo")
def criterios_ensayo(id: str):
    return {"id": id, "criterios": "Criterios de inclusión y exclusión simulados"}

@app.get("/comparar_moleculas")
def comparar_moleculas(molecula1: str, molecula2: str, patologia: str):
    return {"comparación": f"{molecula1} vs {molecula2} en {patologia}"}

@app.get("/analisis_endpoint")
def analisis_endpoint(patologia: str, fase: Optional[str] = None):
    return {"patologia": patologia, "fase": fase, "endpoints_comunes": ["SG", "PFS", "ORR"]}

@app.get("/pico_sugerido")
def pico_sugerido(molecula: str, patologia: str, formato: Optional[str] = "json"):
    pico = {
        "P": f"Pacientes con {patologia}",
        "I": f"{molecula}",
        "C": "Tratamiento estándar o placebo",
        "O": "Supervivencia global, respuesta objetiva"
    }
    if formato == "pdf":
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4
        y = height - 50
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, y, "Formato PICO")
        y -= 30
        c.setFont("Helvetica", 12)
        for k, v in pico.items():
            c.drawString(50, y, f"{k}: {v}")
            y -= 20
        c.save()
        buffer.seek(0)
        return StreamingResponse(buffer, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=pico.pdf"})
    return pico

@app.get("/exportar_ensayos_pdf")
def exportar_ensayos_pdf(molecula: str, patologia: Optional[str] = None):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    c.drawString(50, 800, f"Exportación en PDF para {molecula} / {patologia}")
    c.save()
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="application/pdf", headers={"Content-Disposition": f"attachment;filename=ensayos_{molecula}.pdf"})

@app.get("/exportar_ensayos_csv")
def exportar_ensayos_csv(molecula: str, patologia: Optional[str] = None):
    csv_data = "ID,Título,Fase\nNCT001,Ensayo 1,Fase III\nNCT002,Ensayo 2,Fase II"
    return StreamingResponse(io.BytesIO(csv_data.encode()), media_type="text/csv", headers={"Content-Disposition": f"attachment;filename=ensayos_{molecula}.csv"})

@app.get("/resumen_molecula")
def resumen_molecula(molecula: str, patologia: str):
    return {"molécula": molecula, "patología": patologia, "ensayos_encontrados": 8, "fases": ["Fase II", "Fase III"]}

@app.get("/tendencias_investigacion")
def tendencias_investigacion(patologia: str, año_inicio: Optional[int] = None):
    return {"patologia": patologia, "desde": año_inicio, "tendencias": {"inmunoterapia": "↑", "fase I": 10}}

@app.get("/top_centros")
def top_centros(patologia: str, pais: Optional[str] = None):
    return {"patologia": patologia, "pais": pais, "centros": [{"nombre": "Hospital A", "ensayos": 12}]}

@app.get("/cambios_estado_recientes")
def cambios_estado(patologia: Optional[str] = None, dias: Optional[int] = None):
    return {"patologia": patologia, "dias": dias, "cambios": [{"id": "NCT123", "nuevo_estado": "Reclutando"}]}

@app.get("/mecanismos_accion")
def mecanismos_accion(patologia: str):
    return {"patologia": patologia, "mecanismos": ["Inhibidor de tirosina quinasa", "Anti PD-L1"]}

@app.get("/mapa_investigacion")
def mapa_investigacion(patologia: str):
    return {"patologia": patologia, "distribución": {"España": 12, "Francia": 8}}

@app.get("/moleculas_por_fase")
def moleculas_por_fase(fase: str, patologia: Optional[str] = None):
    return {"fase": fase, "patologia": patologia, "moleculas": ["molécula A", "molécula B"]}

@app.get("/ver_ensayos_por_biomarcador")
def ver_ensayos_por_biomarcador(biomarcador: str, patologia: Optional[str] = None):
    return {"biomarcador": biomarcador, "ensayos": [{"id": "NCT888", "titulo": "Estudio ALK+", "fase": "II"}]}

@app.get("/resumen_terapeutico")
def resumen_terapeutico(molecula: str, patologia: str):
    return {"molecula": molecula, "patologia": patologia, "resumen": "Actúa mediante inhibición de XYZ..."}

@app.get("/evaluacion_evidencia")
def evaluacion_evidencia(molecula: str, patologia: str):
    return {"molecula": molecula, "patologia": patologia, "nivel": "Alta", "rationale": "Fase III con endpoint duro"}

@app.get("/coste_efectividad")
def coste_efectividad(molecula: str, patologia: str, pais: Optional[str] = None):
    return {"molecula": molecula, "patologia": patologia, "pais": pais or "Global", "ICER_estimado": "45.000€/AVAC", "comentario": "Coste-efectivo según umbral local"}
