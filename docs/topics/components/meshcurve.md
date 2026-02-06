# MeshCurve

MeshCurve generates a baked mesh (and optional collider) along a path defined by `PathPoint` components. It is ideal for fences, walls, pipes, and road-like meshes that must follow a curve.

## Create a MeshCurve (Editor shortcuts)

There are two fast ways to create a MeshCurve in the editor:

1. **Topbar → Create Object → MeshCurve**  
   Creates a MeshCurve with the standard `Mesh` and `Points` children.

2. **Files panel → Object file → Create curve of**  
   Right-click (or open the menu on) an object file and choose **Create curve of**.  
   This builds a MeshCurve and automatically places the selected object under the `Mesh` child.

## Typical Setup

1. Create a GameObject and add `MeshCurve`.
2. Add a child named `Mesh` and place your source mesh(es) under it.
3. Add a child named `Points` and create `PathPoint` objects under it.
4. (Optional) Add `StickToTerrain` to the points to keep them on the terrain.

MeshCurve reads the `Mesh` child as the source and the `Points` child as the path.

## Editor Workflow

1. Add at least two `PathPoint` objects under `Points`.
2. Move points to shape the curve.
3. Adjust `Spacing`, `Spacing Padding`, `Forward Axis`, and `Up Mode` on the MeshCurve.
4. Toggle `Fit Curve` if you want the mesh scaled along the path to close the remaining gap.
5. Toggle `Stick To Terrain` if points should snap to terrain.

:::tip
If `Bake Mode` is set to `Static`, the MeshCurve will remove its children after the bake when the game is running. This leaves only the baked mesh and collider for best performance.
:::

## Tips

- Ensure your mesh pivot is centered and aligned with the chosen `Forward Axis`.
- Use `Spacing Padding` for additional gaps between instances.
- If you want no deformation beyond the path limits, keep the mesh fully inside the path length.
