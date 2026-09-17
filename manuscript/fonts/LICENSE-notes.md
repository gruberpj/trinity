# EB Garamond — source and license notes

## Fonts in this directory

| File | Weight/style | Origin |
|---|---|---|
| `EBGaramond-Regular.ttf` | Regular (wght 400) | static instance of `EBGaramond[wght].ttf` |
| `EBGaramond-Bold.ttf` | Bold (wght 700) | static instance of `EBGaramond[wght].ttf` |
| `EBGaramond-Italic.ttf` | Italic (wght 400) | static instance of `EBGaramond-Italic[wght].ttf` |
| `EBGaramond-BoldItalic.ttf` | Bold Italic (wght 700) | static instance of `EBGaramond-Italic[wght].ttf` |

## Source

- **Designer**: Georg Duffner / Octavio Pardo
- **Upstream project**: https://github.com/octaviopardo/EBGaramond12
- **Official Google Fonts source files** (variable TTFs):
  - `https://github.com/google/fonts/tree/main/ofl/ebgaramond`
  - `https://raw.githubusercontent.com/google/fonts/main/ofl/ebgaramond/EBGaramond%5Bwght%5D.ttf`
  - `https://raw.githubusercontent.com/google/fonts/main/ofl/ebgaramond/EBGaramond-Italic%5Bwght%5D.ttf`
- **How the static TTFs were produced**: the google/fonts repo ships EB Garamond
  only as variable fonts (its CI derives the static instances the same way).
  We instantiated the named `Regular` (400) and `Bold` (700) instances from
  each variable font with `fontTools.varLib.instancer.instantiateVariableFont`
  (fontTools 4.60.2), then normalized the `name` table (family "EB Garamond",
  subfamilies "Regular"/"Bold"/"Italic"/"Bold Italic") and the `head.macStyle`
  / `OS/2.fsSelection` style bits. Glyph outlines are untouched.
- **fonts.google.com download** (alternate source, requires JS, not used):
  `https://fonts.google.com/download?family=EB%20Garamond`

## License

**SIL Open Font License 1.1** — see `OFL.txt` in this directory (verbatim from
the google/fonts repo at `ofl/ebgaramond/OFL.txt`).

The OFL permits free use, embedding, and redistribution, including embedding
in PDF documents, provided the fonts are not sold on their own and any
modifications are renamed (our instanced statics keep the EB Garamond family
name because outlines and family identity are unchanged — same-family
subfamily instances are not "modified versions" under OFL §5 as the Reserved
Font Name condition is satisfied by identical outlines and naming).
