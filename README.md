# Game maps as OBJ meshes

This repository contains various OBJ files exported from
[Sauerbraten](https://sauerbraten.org), [Red Eclipse](https://www.redeclipse.net)
and [Tesseract](https://tesseract.gg). These maps were exported using the
`/writeobj <destination>` command after loading the map in the game.

Looking for the cmvalley map exported as an OBJ file? Head to the
[Releases](https://github.com/Calinou/game-maps-obj/releases/latest) tab.

## Caveats

- Maps are exported at a larger scale than you probably want.
  This may cause large maps not to appear at all once imported due to
  view frustum culling. To solve this, tell the engine to import the OBJ mesh
  at a lower scale if possible. Otherwise, you can scale the OBJ mesh by a
  factor of about 0.1. (This may reduce mesh precision, which is why scaling
  at import-time should be preferred.)
- Due to how maps are designed in Cube 2 engine games, their topology may be
  inefficient or otherwise unusual. This could lead to issues when generating
  collision meshes automatically.

## License

See `.txt` files associated with each map for the license.

All maps in the `redeclipse/` and `tesseract/` folders are under free culture
Creative Commons licenses (with commercial use and modification allowed).
In those folders, CC BY-SA is the strictest license used, although some maps
are under CC BY or CC0 instead.

**Warning:** Some maps in the `sauerbraten/` folder use Creative Commons licenses
that disallow commercial use. Still, modification is allowed as maps that use a
no-derivatives license were excluded from this set.
