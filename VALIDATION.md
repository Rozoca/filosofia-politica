# Validación · 2 octubre 2026

## Estado de entrega
**Publicada y verificada el 3 de octubre de 2026.** Integración mediante PR #1, commit `51494e3efb8019a5c61b40ebea7b1a94143793c8`. Los 57 archivos remotos coincidían por SHA con la versión local validada. Verificados en la URL pública: portada nueva, carga de 40 preguntas, test completo de cinco respuestas, explicaciones, resultados y persistencia del intento en Mi progreso. El bloqueo del conector se resolvió mediante publicación en el navegador autorizada por el propietario.

## Pruebas realizadas
- Inventario y análisis estático de los 25 HTML originales; resultado final: 32 HTML.
- 18 módulos históricos, un epílogo, 40 preguntas nuevas (2–3 por lectura), 8 casos, 2 dilemas, 2 retos socráticos, 3 ejercicios de transferencia y reto mensual.
- Enlaces y anclas locales, archivos referenciados, IDs, encabezado h1 único, ausencia de páginas huérfanas, esquema y cobertura de preguntas: sin errores.
- Sintaxis de JavaScript original y compartido: sin errores.
- Carga de las 32 páginas en Chromium, a 390 y 1440 px: sin errores de página JavaScript ni desbordamiento horizontal después de corregir la portada.
- Menú móvil, apertura/cierre con Escape, navegación y buscador por temas.
- Test rápido de cinco preguntas con un error deliberado: 4/5 y 80%, explicación y enlace; guardado único del intento.
- Repetición del error: actualiza última respuesta y elimina el error pendiente.
- Examen acumulativo de diez preguntas: no anticipa explicación; muestra 10/10 y 100% al finalizar.
- Filtros combinados, selección por módulo y casos sin coincidencias: botón de inicio deshabilitado cuando corresponde.
- Ocho casos visibles por filtro, cambio a dilemas, borrador persistente tras recargar, autoevaluación y reflexión completada.
- Reto mensual, exportación JSON, reset con confirmación, importación y aviso de almacenamiento corrupto.
- Los 18 tests históricos: 232 respuestas comprobadas, resultado mostrado en todos y ejecución de reinicio sin errores.
- Constructor repetido: salida idempotente, sin duplicar componentes.
- axe-core WCAG 2 A/AA y 2.1 AA sobre el estado inicial de las 32 páginas: se corrigieron los contrastes detectados; no quedan infracciones automatizadas en ese alcance. Esto no equivale a certificación ni a revisión exhaustiva de todos los estados y pestañas.
- Inspección visual de portada, Laboratorio, resultados y Poder & Influencia en capturas móviles/escritorio.

## Enlaces externos
Portal y perfil profesional: HTTP 200. UNESCO y texto French/Raven alojado en MIT: HTTP 200. NobelPrize, DOI de Raven e Influence at Work: las peticiones HEAD devolvieron 403; sus fuentes se localizaron mediante búsqueda, pero no se afirma validación HTTP completa. Un bloqueo de automatización no se contabiliza como 404.

## Límites conocidos
- Progreso local, sin sincronización automática. Exportación/importación manual. Máximo de 100 intentos en historial.
- Tests antiguos funcionan separados del nuevo registro de progreso.
- Casos abiertos se autoevalúan; no existe IA que califique texto libre.
- Mapa por temática, provisional; las preguntas no constituyen una prueba psicométrica validada.
- Teoría ↔ Presente comienza con dos hitos documentados de 2021/2024; no es un servicio de noticias recientes.
- Fase V sigue en preparación. No se inventan módulos ni se presentan como publicados.
- Se conservan estilos locales antiguos; algunas tipografías dependen de Google Fonts y cuentan con alternativas del sistema. Las pruebas funcionales bloquearon recursos externos para verificar esas alternativas.
- Revisión filosófica enfocada en errores evidentes y contenido añadido, no una edición crítica exhaustiva de todo el archivo.
