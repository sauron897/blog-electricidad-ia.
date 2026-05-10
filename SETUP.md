# Setup — Blog Automatizado con Claude Code

## Estructura del sistema

```
blog-electricidad-ia/
├── src/
│   ├── content/
│   │   ├── config.ts          ← esquema de los posts
│   │   └── blog/              ← aquí van los posts .md (el agente escribe aquí)
│   ├── layouts/
│   │   └── BlogPost.astro     ← plantilla visual de cada post
│   └── pages/
│       ├── index.astro        ← portada del blog
│       └── blog/[...slug].astro ← ruta dinámica de cada post
├── agente/
│   ├── publicador.md          ← instrucciones del agente (el "cerebro")
│   └── pipeline.csv           ← lista de ideas (el "editorial")
├── astro.config.mjs
└── package.json
```

---

## Paso 1 — Instalar dependencias

```powershell
cd blog-electricidad-ia
npm install
```

Comprueba que funciona:
```powershell
npm run dev
```
Abre http://localhost:4321 — deberías ver el blog con el post de ejemplo.

---

## Paso 2 — Subir a GitHub

1. Crea un repositorio nuevo en github.com (sin README, sin .gitignore)
2. En la carpeta del proyecto:

```powershell
git init
git add .
git commit -m "inicio: estructura base del blog"
git remote add origin https://github.com/TU_USUARIO/blog-electricidad-ia.git
git push -u origin main
```

---

## Paso 3 — Conectar Vercel para auto-deploy

1. Ve a vercel.com → New Project → importa el repositorio de GitHub
2. Framework: Astro (Vercel lo detecta automáticamente)
3. Deploy — en 2 minutos tienes el blog publicado en internet
4. Cada vez que el agente haga `git push`, Vercel despliega automáticamente en ~1 min

---

## Paso 4 — Programar el agente

En Claude Code, ejecuta:

```
/schedule
```

Cuando te pregunte, dale estas instrucciones:

- **Nombre:** Publicador Blog Electricidad
- **Frecuencia:** diaria (por ejemplo, cada día a las 18:00)
- **Prompt:** Lee el archivo `agente/publicador.md` en el repositorio `blog-electricidad-ia` y ejecuta todas las instrucciones que contiene paso a paso.

---

## Paso 5 — Gestionar el pipeline de ideas

Edita `agente/pipeline.csv` añadiendo ideas nuevas con estado `Pendiente`.

El agente siempre coge la primera fila con estado `Pendiente` y la publica.

**Campos del CSV:**
| Campo | Descripción |
|-------|-------------|
| `idea` | Título o tema del post |
| `keywords_objetivo` | Keyword principal a posicionar |
| `estado` | `Pendiente` o `Publicado` |
| `fecha_publicacion` | Lo rellena el agente |
| `slug` | Lo rellena el agente |

---

## Cómo añadir ideas al pipeline

Abre `agente/pipeline.csv` y añade una línea:

```
Mi nueva idea de post,keyword principal,Pendiente,,
```

Haz commit y push. El agente la cogerá en su próxima ejecución.

---

## Flujo completo (qué pasa cada tarde)

```
[18:00] Claude Code Agent arranca en remoto
    ↓
Lee pipeline.csv → encuentra primera fila "Pendiente"
    ↓
Hace research de keywords con búsqueda web
    ↓
Escribe el post completo en Markdown
    ↓
git push → Vercel detecta el cambio
    ↓
[18:02] Post publicado en internet
    ↓
Marca fila como "Publicado" en pipeline.csv
    ↓
[18:03] Agente finalizado
```

**Tú no intervienes en ningún paso.**

---

## Para actualizar el dominio

Cuando tengas un dominio propio, cambia esta línea en `astro.config.mjs`:

```js
site: 'https://tu-dominio.com',
```

---

## Métricas a seguir (semanal)

- Google Search Console: impresiones y posición media
- Posts publicados vs posts en pipeline
- CTR por post (objetivo: >2%)
- Keywords en posiciones 1-10

Puedes pedirle a Claude Code que analice tus datos de Search Console una vez a la semana.
