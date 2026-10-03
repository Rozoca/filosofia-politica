# Mantener Filosofía & Política

## Qué se ha construido
El portal sigue siendo un sitio estático de GitHub Pages. No requiere servidor de aplicación, cuentas, claves ni instalación de paquetes para funcionar. Las 18 lecturas originales y el epílogo conservan sus páginas, pestañas y tests. El Laboratorio añade una evaluación distinta, transversal.

- `data/modules.json`: catálogo de lecturas, autores, fases, temas y URLs.
- `data/questions.json`: 40 preguntas del Laboratorio.
- `data/cases.json`: 8 casos, 2 dilemas, 2 retos socráticos y 3 transferencias.
- `data/challenges.json`: edición, pregunta y reto del mes.
- `data/topics.json`: las diez categorías transversales.
- `data/power.json`: preguntas, modelos, aplicación y referencias de Poder & Influencia.
- `data/present.json`: hechos fechados, fuentes, interpretaciones y preguntas.
- `assets/js/app.js`: filtros, evaluación, actividades y resultados.
- `assets/js/store.js`: progreso local y criterios del mapa.
- `assets/js/common.js`: menú, visitas y accesibilidad de componentes antiguos.
- `assets/css/portal.css`: componentes compartidos y adaptación móvil.
- `scripts/build.py`: genera las siete páginas nuevas y actualiza navegación, pie, práctica, metadatos y sitemap en todas las páginas. Solo necesita Python 3.
- `scripts/validate.py`: comprueba datos, enlaces/anclas locales, páginas huérfanas y sintaxis JavaScript (requiere Python 3 y Node).
- `scripts/stabilize.py`: registro de la migración inicial. **No volver a ejecutarlo.**

## Antes de tocar nada
1. Obtener los cambios más recientes de `main` y comprobar que no hay cambios sin guardar.
2. Crear una rama con fecha, por ejemplo `update/2026-12`.
3. Anotar el commit base y conservarlo para rollback.
4. Leer `AUDIT.md` y `VALIDATION.md`. No confundir contenido preparado con contenido publicado.

## Añadir una pregunta
En `data/questions.json`, copia un objeto existente y cambia:
- `id`: identificador único y estable; no reutilices el ID para una pregunta diferente.
- `question`: una situación o problema claro.
- `options`: cuatro alternativas plausibles, solo una defendible como mejor respuesta bajo el enunciado.
- `answer`: posición de la respuesta, contando desde **0** (0, 1, 2, 3).
- `explanation`: explica el criterio, el error frecuente y los límites; no solo «correcto».
- `difficulty`: `Básico`, `Intermedio` o `Avanzado`.
- `level`: 1 reconocer, 2 explicar, 3 comparar, 4 aplicar. En elección múltiple, «explicar» solo evalúa reconocer una buena explicación; usa actividades abiertas para producción propia.
- `authors`: lista con los nombres del catálogo.
- `phase`: número de fase publicada.
- `topics`: lista de categorías de `topics.json`.
- `module`: ID de una lectura existente.

La selección combina filtros con AND; un cruce puede no tener preguntas. No se rellenan cupos con preguntas fuera del filtro. Test rápido: hasta 5. Examen: hasta 10. La Fase V no se anuncia como evaluable mientras no tenga módulos publicados.

**Importante:** el validador inicial comprueba 40 preguntas y 8 casos. Al ampliar, sustituye esas comprobaciones de cantidad exacta por el nuevo mínimo acordado; mantén las de unicidad, enlaces y campos obligatorios.

## Añadir casos, dilemas o transferencia
Añade un objeto a `cases.json` con ID único, `kind` (`caso`, `dilema`, `socratico` o `transferencia`), título, escenario, duración, preguntas, perspectivas (`author`, `analysis`), módulos relacionados y transferencia final. Formula una tensión real y explicita qué información falta. Evita convertir autores en caricaturas. La rúbrica es autoevaluación: conceptos/evidencia, perspectivas/límites, objeción y conclusión revisable. No hay corrección automática del texto libre.

## Renovar el mes
En `challenges.json`, cambia `edition` (`AAAA-MM`), `question` y el objeto `challenge`. Usa un ID nuevo para cada edición; así no se confunden reflexiones anteriores con la actividad nueva. Incluye objetivo en el escenario, duración, instrucciones, preguntas, conceptos/módulos y reflexión final. La web muestra que una edición vencida es de archivo; no cambia el contenido fingiendo novedad.

## Actualizar Teoría ↔ Presente
En `present.json`, separa:
1. `fact`: acontecimiento breve verificable.
2. `eventDate`: fecha real del hecho, no de la edición del portal.
3. `reviewed`: fecha de comprobación de la fuente.
4. `source` y `sourceName`: fuente primaria fiable y enlace directo.
5. `interpretations`: al menos dos lecturas cuando proceda.
6. `question`, `limit` y `modules`.

No conviertas una interpretación en hecho ni una previsión en acontecimiento. Revisa enlaces y afirmaciones. Los dos ejemplos iniciales son hitos de 2021 y 2024, no noticias de octubre de 2026.

## Categorías, autores y Poder & Influencia
Para añadir una categoría, inclúyela en `topics.json` y etiqueta lecturas/preguntas. No hace falta una página nueva. Para ampliar poder, añade a `power.json` una pregunta concreta, autor/modelo, idea, práctica y referencia. Ejecuta el constructor para publicar esos cambios. Incorpora un caso de observación cuando aporte algo. El objetivo es comprensión y autonomía, no explotar vulnerabilidades.

## Construir y probar
Desde la carpeta del repositorio:
```bash
python scripts/build.py
python scripts/validate.py
python -m http.server 8000
```
Abre `http://localhost:8000`. No abras los HTML con doble clic: los datos JSON se cargan mediante HTTP. Revisa escritorio y móvil (al menos 390 px), menú y Escape, teclado, filtros sin resultados, test con errores, examen sin feedback anticipado, resultados, borradores y progreso tras recargar. Revisa los tests históricos si cambias componentes compartidos. `build.py` puede ejecutarse varias veces; no debe duplicar componentes.

Para la regresión automatizada de navegador, `scripts/browser-test.cjs` requiere Playwright disponible y un Chromium compatible. Puedes definir `CHROMIUM_PATH` si no usas el Chromium de Playwright. Levanta su propio servidor temporal; ejecuta `node scripts/browser-test.cjs` desde la raíz. No es una dependencia del sitio publicado.

## Publicar en GitHub Pages
1. Validar en la rama de trabajo y crear commits descriptivos.
2. Comparar el diff con el commit base: conservar medios, contenido y cambios de otros colaboradores.
3. Subir la rama y revisar/combinar en la rama que use Pages. Confirmar la configuración real en GitHub; no asumir que la conexión tiene escritura.
4. Esperar a que el despliegue termine correctamente.
5. Abrir `https://rozoca.github.io/filosofia-politica/` y verificar portada, laboratorio, carga de JSON, una actividad y progreso en la URL publicada.
6. Solo entonces marcar la entrega como publicada. Un commit local o un ZIP no equivalen a despliegue.

Si GitHub rechaza la escritura por permisos, arreglar la conexión o utilizar una vía autorizada por el propietario. No sobrescribir la rama remota ni forzar un push para evitar un conflicto.

## Rollback
Base anterior a esta evolución: `dd1a538c61af70ada31b42ef2de3ae44de69ffcb`. Rama local: `rollback/pre-learning-2026-10-02`. Si ya se publicó, es preferible revertir los commits de evolución con nuevos commits y volver a desplegar, preservando historial. No usar `reset --hard` ni `push --force` sobre trabajo ajeno. El fichero bundle entregado conserva el historial local y la referencia de respaldo.

## Progreso y privacidad
Clave localStorage: `fp-learning-v1`; esquema `version: 1`. Visitas no equivalen a lecturas completadas. Se guardan los últimos 100 intentos; el mapa usa la última respuesta a cada pregunta y exige tres preguntas distintas por tema. Las fortalezas son provisionales, no una acreditación. Los tests antiguos no se incorporan al mapa. Los borradores y autoevaluaciones son locales, no se envían a un backend. Exportar/importar permite trasladar datos entre dispositivos; no hay sincronización automática. Borrar el almacenamiento del navegador elimina el progreso. No reutilizar IDs; al cambiar el esquema, crear una migración y probarla.

## Prompt de actualización periódica
> Actualiza mi portal Filosofía & Política en Rozoca/filosofia-politica. Lee MAINTENANCE.md, AUDIT.md y VALIDATION.md; inspecciona el estado actual y los cambios de otros colaboradores. Conserva una referencia para rollback. Mantén la identidad editorial, las páginas históricas y GitHub Pages. Añade 10–20 preguntas de calidad, priorizando temas y niveles con poca cobertura; añade 2–3 casos con perspectivas y rúbrica. Renueva la pregunta y el reto del mes con IDs nuevos. Actualiza Teoría ↔ Presente con fuentes verificadas y fechas, separando hechos, interpretaciones y preguntas. Amplía Poder & Influencia solo alrededor de un problema concreto. Modifica los JSON, ejecuta el constructor y revisa el diff. Valida enlaces, móvil, escritorio, accesibilidad, tests, filtros, borradores, progreso y consola. Conserva compatibilidad con el progreso anterior. Publica por la vía autorizada, verifica la URL en vivo y entrega un resumen de cambios, pruebas, límites y próximos pasos. Si falta un permiso, completa primero lo verificable e identifica exactamente el bloqueo; no declares publicado lo que no lo está.
