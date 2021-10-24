


import maya.cmds as cmds

cmds.polySphere(radius=3,
                subdivisionsX=20,
                subdivisionsY=20,
                axis =[0,0,0],
                createUVs=2,
                constructionHistory=1)

cmds.move( 0, 0, 0 )


cmds.polySphere(radius=2,
                subdivisionsX=20,
                subdivisionsY=20,
                axis =[3,0,0],
                createUVs=2,
                constructionHistory=1)
cmds.move( 0, 3, 0 )

cmds.polySphere(radius=1,
                subdivisionsX=20,
                subdivisionsY=20,
                axis =[0,1,0],
                createUVs=2,
                constructionHistory=1)
cmds.move( 0, 5, 0 )


cmds.polySphere(radius=.2,
                subdivisionsX=20,
                subdivisionsY=20,
                axis =[0,1,0],
                createUVs=2,
                constructionHistory=1)
cmds.move( -.339, 5.59, 0.7 )



cmds.polySphere(radius=.2,
                subdivisionsX=20,
                subdivisionsY=20,
                axis =[0,1,0],
                createUVs=2,
                constructionHistory=1)
cmds.move( .498, 5.59, .64 )

cmds.polyCube(
                subdivisionsX=4,
                subdivisionsY=4,
                axis =[0,1,0],
                h = 1,
                w = 1,
                d = 1 ,
                createUVs=2,
                constructionHistory=1)

cmds.move( 0, 6.7, 0 )

cmds.polyCube(
                subdivisionsX=4,
                subdivisionsY=4,
                axis =[0,1,0],
                h = .5,
                w = 2,
                d = 2 ,
                createUVs=2,
                constructionHistory=1)

cmds.move( 0, 6, 0 )

cmds.polySphere(radius=.1,
                subdivisionsX=20,
                subdivisionsY=20,
                axis =[3,0,0],
                createUVs=2,
                constructionHistory=1)
cmds.move( 0, 5.21, 1 )

cmds.polyCube(
                subdivisionsX=4,
                subdivisionsY=4,
                axis =[0,1,0],
                h = .5,
                w = 5,
                d = .5 ,
                createUVs=2,
                constructionHistory=1)

cmds.move( -2.58, 3.7, 0 )
cmds.move( -2.58, 3.7, 0 )

cmds.polyCube(
                subdivisionsX=4,
                subdivisionsY=4,
                axis =[0,1,0],
                h = .5,
                w = 5,
                d = .5 ,
                createUVs=2,
                constructionHistory=1)

cmds.move( 2.49, 3.79, 0 )