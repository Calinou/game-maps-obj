# Game maps as OBJ meshes

This repository contains various OBJ files exported from
[Sauerbraten](https://sauerbraten.org), [Red Eclipse](https://www.redeclipse.net)
and [Tesseract](https://tesseract.gg). These maps were exported using the
`/writeobj <destination>` command after loading the map in the game.

Looking for the cmvalley map exported as an OBJ file? Head to the
[Releases](https://github.com/Calinou/game-maps-obj/releases/latest) tab.

## Games

Maps were exported from the following games:

- **Red Eclipse** (commit [`ecfe18c51`](https://github.com/redeclipse/maps/commit/ecfe18c51ffa192ca127920170ea7f33b99c2dd2))
- **Sauerbraten** (SVN revision 5980)
- **Tesseract** (SVN revision 2343)

## Recommended maps

Here are some hand-picked recommendations if you'd like to try out some maps:

|            Name | Vertex/triangle count   | Good for                                                         | License         |
|----------------:|:------------------------|:-----------------------------------------------------------------|:----------------|
|       cmvalley¹ | 1112k verts, 2080k tris | Testing renderers in a large scale/open world map                | CC BY 4.0       |
|   core_transfer | 45k verts, 76k tris     | Testing global illumination and fog                              | CC BY-NC-SA 2.5 |
|  eternal_valley | 55k verts, 98k tris     | Testing global illumination and its resistance to leaks          | CC BY-NC-SA 3.0 |
|             fc4 | 44k verts, 80k tris     | Testing renderers over a fairly large area (with inland terrain) | CC BY-NC-SA 3.0 |
|             fc5 | 103k verts, 189k tris   | Testing renderers over a fairly large area (mostly buildings)    | CC BY-NC-SA 3.0 |
|          hidden | 105k verts, 190k tris   | Testing renderers over a fairly large area (mostly buildings)    | CC BY-NC-SA 3.0 |
|          k_rpg1 | 136k verts, 261k tris   | Testing renderers in a large scale/open world map                | CC BY-NC-SA 2.5 |
|         octavus | 52k verts, 86k tris     | Testing renderers over a fairly large area (with smooth terrain) | CC BY-SA 3.0    |
|         pandora | 36k verts, 61k tris     | Testing lighting in a fully indoor level                         | CC BY 4.0       |
|      reflection | 68k verts, 116k tris    | Testing global illumination and fog (indoors with sunlight)      | CC BY-SA 3.0    |
|          skrsp1 | 59k verts, 103k tris    | Testing renderers over a fairly large area (with terrain)        | CC BY-NC-SA 3.0 |
|       steelribs | 27k verts, 46k tris     | Testing renderers with a floating hard-surface map               | CC BY-SA 3.0    |
|        tectonic | 47k verts, 87k tris     | Testing renderers with an island-style map (buildings + terrain) | CC BY 4.0       |
|            ubik | 87k verts, 166k tris    | Testing renderers with a floating futuristic urban area          | CC BY-SA 3.0    |

¹: cmvalley can be downloaded from the [Releases](https://github.com/Calinou/game-maps-obj/releases/latest) tab.

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
- Maps don't contain mapmodels (detail models such as trees, barrels, …) and
  materials (such as water, lava and glass). You will have to readd those
  manually if desired.

## License

See `.txt` files associated with each map for the license.

All maps in the `redeclipse/` and `tesseract/` folders are under free culture
Creative Commons licenses (with commercial use and modification allowed).
In those folders, CC BY-SA is the strictest license used, although some maps
are under CC BY or CC0 instead.

**Warning:** Some maps in the `sauerbraten/` folder use Creative Commons licenses
that disallow commercial use. Still, modification is allowed as maps that use a
no-derivatives license were excluded from this set.
