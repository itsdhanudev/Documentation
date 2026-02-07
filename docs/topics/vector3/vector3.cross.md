
# `Vector3.cross`

## Signature

```java
Vector3 cross(Vector3 v)
```

## Summary

Returns the cross product of this vector and another vector.

## Description

The cross product results in a third vector that is perpendicular to both input vectors. This is commonly used to find a normal vector to a surface, determine the axis of rotation between two directions, or establish a coordinate system.

The resulting vector points in a direction determined by the right-hand rule: if you point your index finger along the first vector and your middle finger along the second vector, your thumb points in the direction of the cross product.

The cross product is not commutative, meaning `a.cross(b)` is not the same as `b.cross(a)`. In fact, `b.cross(a)` points in the opposite direction.

## Example

```java
public SpatialObject objectA;
public SpatialObject objectB;

/// Run only once
void start() {}

/// Repeat every frame
void repeat() {
  // Get two vectors from current position to two objects
  Vector3 side1 = (objectA.getPosition() - myTransform.getPosition()).normalize();
  Vector3 side2 = (objectB.getPosition() - myTransform.getPosition()).normalize();
  
  // Calculate perpendicular vector (surface normal)
  Vector3 normal = side1.cross(side2).normalize();
  
  print("Normal direction: " + normal);
}
```

## Return Value

**Vector3**: A vector perpendicular to both input vectors. The magnitude depends on the angle between the vectors and their lengths.

## Common Usage Patterns

**Finding surface normals**: Calculate the normal to a triangle or plane.

```java
Vector3 getSurfaceNormal(Vector3 pointA, Vector3 pointB, Vector3 origin) {
  Vector3 edge1 = pointA - origin;
  Vector3 edge2 = pointB - origin;
  return edge1.cross(edge2).normalize();
}
```

**Creating perpendicular vectors**: Generate a vector perpendicular to a given direction.

```java
Vector3 forward = myTransform.forward();
Vector3 right = forward.cross(new Vector3(0, 1, 0)).normalize();
```

**Determining rotation axis**: Find the axis around which one vector rotates to another.

```java
Vector3 currentDir = myTransform.forward();
Vector3 targetDir = (target.getPosition() - myTransform.getPosition()).normalize();
Vector3 rotationAxis = currentDir.cross(targetDir).normalize();
```

**Left or right detection**: Determine if a point is to the left or right of a direction.

```java
Vector3 forward = myTransform.forward();
Vector3 toTarget = (target.getPosition() - myTransform.getPosition()).normalize();
Vector3 perpendicular = forward.cross(toTarget);

if (perpendicular.y > 0) {
  print("Target is to the right");
} else {
  print("Target is to the left");
}
```
<div style={{ width: "100%", aspectRatio: "1 / 1" }}>
  <iframe
    src="https://rawcdn.githack.com/ITsMagic-Software/Documentation/main/static/hpages/vector3.cross.vis.html"
    style={{ width: "100%", height: "100%", border: "none" }}
  />
</div>
