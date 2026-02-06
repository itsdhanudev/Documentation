# MeshCurve

MeshCurve gera um mesh baked (e opcionalmente um collider) ao longo de um caminho definido por componentes `PathPoint`. Ele é ideal para cercas, paredes, tubos e meshes do tipo estrada que precisam seguir uma curva.

## Criar um MeshCurve (atalhos no editor)

Existem duas formas rápidas de criar um MeshCurve no editor:

1. **Topbar → Criar objeto → MeshCurve**  
   Cria um MeshCurve com os filhos padrão `Mesh` e `Points`.

2. **Painel Files → Arquivo de objeto → Create curve of**  
   Clique no menu do arquivo de objeto e escolha **Create curve of**.  
   Isso cria um MeshCurve e coloca automaticamente o objeto selecionado dentro do filho `Mesh`.

## Configuração típica

1. Crie um GameObject e adicione `MeshCurve`.
2. Adicione um filho chamado `Mesh` e coloque o(s) mesh(es) de origem dentro dele.
3. Adicione um filho chamado `Points` e crie objetos `PathPoint` dentro dele.
4. (Opcional) Adicione `StickToTerrain` aos pontos para manter no terreno.

O MeshCurve usa o filho `Mesh` como origem e o filho `Points` como caminho.

## Fluxo no Editor

1. Adicione pelo menos dois objetos `PathPoint` dentro de `Points`.
2. Mova os pontos para moldar a curva.
3. Ajuste `Spacing`, `Spacing Padding`, `Forward Axis` e `Up Mode` no MeshCurve.
4. Ative `Fit Curve` se quiser escalar o mesh ao longo do path para fechar o espaço restante.
5. Ative `Stick To Terrain` se os pontos devem ficar colados no terreno.

:::tip
Se `Bake Mode` estiver em `Static`, o MeshCurve remove os filhos após o bake quando o jogo estiver rodando. Assim restam apenas o mesh e o collider baked para melhor performance.
:::

## Dicas

- Garanta que o pivot do mesh esteja centralizado e alinhado com o `Forward Axis`.
- Use `Spacing Padding` para criar espaçamentos extras entre instâncias.
- Se não quiser deformação fora do path, mantenha o mesh totalmente dentro do comprimento do path.
