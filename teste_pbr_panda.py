
import os
import math

from direct.showbase.ShowBase import ShowBase
import panda3d.core as p3d
import simplepbr


class LuminaTest(ShowBase):

    def __init__(self):
        super().__init__()

        # Renderizador PBR
        self.pipeline = simplepbr.init()

        self.setBackgroundColor(0.38, 0.44, 0.52, 1)

        # Caminho do personagem
        path = os.path.abspath(
            "assets/models/characters/Knight_Male.gltf"
        )

        infile = p3d.Filename.from_os_specific(path)

        p3d.get_model_path().prepend_directory(
            infile.get_dirname()
        )

        # Carregamento nativo do glTF
        self.model_root = self.loader.load_model(
            infile,
            noCache=True
        )

        self.model_root.reparent_to(self.render)

        # Enquadrar personagem
        bounds = self.model_root.getBounds()
        center = bounds.get_center()
        radius = max(bounds.get_radius(), 0.1)

        fov = self.camLens.get_fov()

        distance = radius / math.tan(
            math.radians(min(fov[0], fov[1]) / 2)
        )

        self.camLens.set_near(min(0.1, radius / 2))
        self.camLens.set_far(distance + radius * 3)

        trackball = self.trackball.node()
        trackball.set_origin(center)
        trackball.set_pos(0, distance, 0)
        trackball.setForwardScale(distance * 0.006)

        # Iluminacao principal
        if not self.model_root.find("**/+Light"):
            self.light = self.render.attach_new_node(
                p3d.PointLight("light")
            )
            self.light.set_pos(0, -distance, distance)
            self.render.set_light(self.light)

        # Preservar as luzes do modelo, se houver
        self.model_root.clear_light()

        for light in self.model_root.find_all_matches(
            "**/+Light"
        ):
            light.parent.wrt_reparent_to(self.render)
            self.render.set_light(light)

        # Luz ambiente
        self.ambient = self.render.attach_new_node(
            p3d.AmbientLight("ambient")
        )

        self.ambient.node().set_color((0.2, 0.2, 0.2, 1))
        self.render.set_light(self.ambient)

        # Detectar e reproduzir animacoes
        self.anims = p3d.AnimControlCollection()

        if self.model_root.find("**/+Character"):
            p3d.autoBind(
                self.model_root.node(),
                self.anims,
                ~0
            )

            if self.anims.get_num_anims() > 0:
                self.anims.get_anim(0).loop(True)

        print("Modelo carregado!")
        print("Animacoes encontradas:", self.anims.get_num_anims())

        self.accept("escape", self.userExit)


LuminaTest().run()
