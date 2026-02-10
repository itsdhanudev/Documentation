# `Vector3.cross`

## Assinatura

```java
Vector3 cross(Vector3 v)
```

## Resumo

Retorna o produto vetorial deste vetor e outro vetor.

## Descrição

O produto vetorial resulta em um terceiro vetor que é perpendicular a ambos os vetores de entrada. Isso é comumente usado para encontrar um vetor normal a uma superfície, determinar o eixo de rotação entre duas direções ou estabelecer um sistema de coordenadas.

O vetor resultante aponta em uma direção determinada pela regra da mão direita: se você apontar seu dedo indicador ao longo do primeiro vetor e seu dedo médio ao longo do segundo vetor, seu polegar aponta na direção do produto vetorial.

O produto vetorial não é comutativo, o que significa que `a.cross(b)` não é o mesmo que `b.cross(a)`. Na verdade, `b.cross(a)` aponta na direção oposta.

## Exemplo

```java
public SpatialObject objectA;
public SpatialObject objectB;

/// Executa apenas uma vez
void start() {}

/// Repete a cada frame
void repeat() {
  // Obtém dois vetores da posição atual para dois objetos
  Vector3 side1 = (objectA.getPosition() - myTransform.getPosition()).normalize();
  Vector3 side2 = (objectB.getPosition() - myTransform.getPosition()).normalize();
  
  // Calcula vetor perpendicular (normal da superfície)
  Vector3 normal = side1.cross(side2).normalize();
  
  print("Direção normal: " + normal);
}
```

## Valor de Retorno

**Vector3**: Um vetor perpendicular a ambos os vetores de entrada. A magnitude depende do ângulo entre os vetores e seus comprimentos.

## Padrões de Uso Comuns

**Encontrar normais de superfície**: Calcula a normal de um triângulo ou plano.

```java
Vector3 getSurfaceNormal(Vector3 pointA, Vector3 pointB, Vector3 origin) {
  Vector3 edge1 = pointA - origin;
  Vector3 edge2 = pointB - origin;
  return edge1.cross(edge2).normalize();
}
```

**Criar vetores perpendiculares**: Gera um vetor perpendicular a uma direção dada.

```java
Vector3 forward = myTransform.forward();
Vector3 right = forward.cross(new Vector3(0, 1, 0)).normalize();
```

**Determinar eixo de rotação**: Encontra o eixo em torno do qual um vetor gira para outro.

```java
Vector3 currentDir = myTransform.forward();
Vector3 targetDir = (target.getPosition() - myTransform.getPosition()).normalize();
Vector3 rotationAxis = currentDir.cross(targetDir).normalize();
```

**Detecção de esquerda ou direita**: Determina se um ponto está à esquerda ou à direita de uma direção.

```java
Vector3 forward = myTransform.forward();
Vector3 toTarget = (target.getPosition() - myTransform.getPosition()).normalize();
Vector3 perpendicular = forward.cross(toTarget);

if (perpendicular.y > 0) {
  print("Alvo está à direita");
} else {
  print("Alvo está à esquerda");
}
```
<div style={{ width: "100%", aspectRatio: "1 / 1" }}>
  <iframe
    src="https://rawcdn.githack.com/ITsMagic-Software/Documentation/main/static/hpages/vector3.cross.vis.html"
    style={{ width: "100%", height: "100%", border: "none" }}
  />
</div>
