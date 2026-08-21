# Sitio del curso: Estadística y Machine Learning para Estudiantes de Medicina

Sitio estático listo para GitHub Pages. Contiene:

- `index.html`: la página completa (autocontenida, con modo claro y oscuro automático).
- `syllabus.pdf`: el syllabus compartible, enlazado desde la página.

## Publicarlo en GitHub Pages (5 minutos, sin terminal)

1. Entra a github.com con tu cuenta y crea un repositorio nuevo, público, llamado por ejemplo `curso-datos-medicina`.
2. En el repositorio: **Add file → Upload files**, arrastra `index.html` y `syllabus.pdf`, y presiona **Commit changes**.
3. Ve a **Settings → Pages**. En "Build and deployment", Source: **Deploy from a branch**; Branch: **main** y carpeta **/ (root)**. Guarda.
4. Espera 1 a 2 minutos. Tu página quedará en: `https://TU-USUARIO.github.io/curso-datos-medicina/`

## Publicarlo con la terminal (si tienes GitHub CLI)

```bash
cd carpeta-del-sitio
git init && git add . && git commit -m "Sitio del curso"
gh repo create curso-datos-medicina --public --source=. --push
gh api repos/{owner}/curso-datos-medicina/pages -X POST -f "source[branch]=main" -f "source[path]=/"
```

## Conectar el Google Form

Cuando tengas el enlace del formulario, abre `index.html`, busca al final:

```js
var FORM_URL = "";
```

y pega el enlace entre las comillas. Sube el archivo actualizado al repositorio (Upload files → reemplazar). Mientras `FORM_URL` esté vacío, el botón de inscripción lleva a tu WhatsApp.

## Actualizar el syllabus

Reemplaza `syllabus.pdf` por la nueva versión con el mismo nombre y súbelo al repositorio.
