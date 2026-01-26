"""
Example ManimGL Scenes
Run with: manimgl scenes/example_scenes.py <SceneName>

Examples:
    manimgl scenes/example_scenes.py HelloWorld
    manimgl scenes/example_scenes.py BasicShapes
    manimgl scenes/example_scenes.py MathEquations
    manimgl scenes/example_scenes.py WaveAnimation

Add -w flag to save to file:
    manimgl scenes/example_scenes.py HelloWorld -w
"""

from manimlib import *


class HelloWorld(Scene):
    """Simple hello world scene to verify ManimGL installation."""

    def construct(self):
        text = Text("Hello, ManimGL!", font_size=72)
        text.set_color_by_gradient(BLUE, GREEN)

        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))


class BasicShapes(Scene):
    """Demonstrates basic geometric shapes and transformations."""

    def construct(self):
        # Create shapes
        circle = Circle(radius=1, color=BLUE)
        square = Square(side_length=2, color=GREEN)
        triangle = Triangle(color=RED)

        # Position shapes
        circle.shift(LEFT * 3)
        triangle.shift(RIGHT * 3)

        # Animate creation
        self.play(
            ShowCreation(circle),
            ShowCreation(square),
            ShowCreation(triangle),
        )
        self.wait(1)

        # Transform square to circle
        self.play(Transform(square, circle.copy().move_to(ORIGIN)))
        self.wait(1)

        # Rotate all shapes
        self.play(
            Rotate(circle, angle=TAU),
            Rotate(square, angle=TAU),
            Rotate(triangle, angle=TAU),
            run_time=2
        )
        self.wait(1)


class MathEquations(Scene):
    """Shows mathematical equations with LaTeX."""

    def construct(self):
        # Euler's identity
        euler = Tex(
            "e^{i\\pi} + 1 = 0",
            font_size=72
        )
        euler_label = Text("Euler's Identity", font_size=36)
        euler_label.next_to(euler, DOWN, buff=0.5)

        self.play(Write(euler))
        self.play(FadeIn(euler_label, shift=UP))
        self.wait(2)

        # Transform to quadratic formula
        self.play(FadeOut(euler_label))

        quadratic = Tex(
            "x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}",
            font_size=60
        )
        quad_label = Text("Quadratic Formula", font_size=36)
        quad_label.next_to(quadratic, DOWN, buff=0.5)

        self.play(Transform(euler, quadratic))
        self.play(FadeIn(quad_label, shift=UP))
        self.wait(2)


class WaveAnimation(Scene):
    """Animates a sine wave - complements the audio visualizer theme."""

    def construct(self):
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=4,
        )

        # Create the initial sine wave
        wave = axes.get_graph(
            lambda x: np.sin(x),
            color=BLUE
        )

        wave_label = Tex("y = \\sin(x)", font_size=48)
        wave_label.to_corner(UR)

        self.play(ShowCreation(axes))
        self.play(ShowCreation(wave), Write(wave_label))
        self.wait(1)

        # Animate wave transformation
        for freq in [2, 3, 1]:
            new_wave = axes.get_graph(
                lambda x, f=freq: np.sin(f * x),
                color=BLUE if freq == 1 else (GREEN if freq == 2 else RED)
            )
            new_label = Tex(f"y = \\sin({freq}x)", font_size=48)
            new_label.to_corner(UR)

            self.play(
                Transform(wave, new_wave),
                Transform(wave_label, new_label),
                run_time=1.5
            )
            self.wait(0.5)

        self.wait(1)


class ThreeDScene(ThreeDScene):
    """Demonstrates 3D capabilities of ManimGL."""

    def construct(self):
        # Create 3D axes
        axes = ThreeDAxes()

        # Create a 3D surface
        surface = Surface(
            lambda u, v: np.array([
                u,
                v,
                np.sin(u) * np.cos(v)
            ]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(30, 30),
        )
        surface.set_color_by_gradient(BLUE, GREEN, YELLOW)

        # Set camera orientation
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)

        self.play(ShowCreation(axes))
        self.play(ShowCreation(surface), run_time=3)

        # Rotate camera around the scene
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()


class InteractiveDemo(Scene):
    """Interactive scene - use mouse and keyboard during playback."""

    def construct(self):
        text = Text(
            "ManimGL Interactive Mode\n\n"
            "Press 'q' to quit\n"
            "Press 'r' to reset\n"
            "Use mouse to pan/zoom",
            font_size=36,
            line_spacing=1.5
        )
        text.set_color_by_gradient(BLUE, PURPLE)

        self.play(Write(text))
        self.wait()

        # This allows interaction in the window
        self.embed()
