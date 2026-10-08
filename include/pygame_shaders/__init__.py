import os
import sys
import pygame

MOBILE_RUNTIME = os.environ.get("FNAH_MOBILE") == "1" or sys.platform in ("android", "ios")

if MOBILE_RUNTIME:
    DEFAULT_VERTEX_SHADER = ""
    DEFAULT_FRAGMENT_SHADER = ""

    class Shader:
        """SDL2 fallback used on mobile where desktop ModernGL is unavailable."""

        def __init__(self, vertex_path, fragment_path, target_surface):
            self.target_surface = target_surface

        def render_direct(self, rect, update_surface=True):
            display = pygame.display.get_surface()
            if display is not self.target_surface:
                display.blit(self.target_surface, (0, 0))

    class DefaultScreenShader(Shader):
        pass

    class ComputeShader:
        def __init__(self, *args, **kwargs):
            raise RuntimeError("Compute shaders are unavailable in mobile SDL2 mode")
else:
    from include.pygame_shaders.pygame_shaders import Shader
    from include.pygame_shaders.pygame_shaders import DefaultScreenShader
    from include.pygame_shaders.pygame_shaders import ComputeShader
    from include.pygame_shaders.pygame_shaders import DEFAULT_FRAGMENT_SHADER
    from include.pygame_shaders.pygame_shaders import DEFAULT_VERTEX_SHADER
    from include.pygame_shaders.texture import Texture
