"""
Example ManimGL Scenes
Run with: manimgl scenes/example_scenes.py <SceneName>

Examples:
    manimgl scenes/example_scenes.py HelloWorld
    manimgl scenes/example_scenes.py BasicShapes
    manimgl scenes/example_scenes.py MathEquations
    manimgl scenes/example_scenes.py WaveAnimation
    manimgl scenes/example_scenes.py TriangleAnimation
    manimgl scenes/example_scenes.py Rule30Hypergraph

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


class TriangleAnimation(Scene):
    """Animates a triangle with various transformations."""

    def construct(self):
        # Create a triangle
        triangle = Triangle(color=BLUE)
        triangle.set_fill(BLUE, opacity=0.5)
        triangle.scale(2)

        # Draw the triangle
        self.play(ShowCreation(triangle), run_time=1.5)
        self.wait(0.5)

        # Rotate the triangle
        self.play(Rotate(triangle, angle=TAU), run_time=2)
        self.wait(0.5)

        # Change color with gradient
        self.play(
            triangle.animate.set_color_by_gradient(RED, YELLOW, GREEN),
            run_time=1
        )
        self.wait(0.5)

        # Scale up and down
        self.play(triangle.animate.scale(1.5), run_time=0.5)
        self.play(triangle.animate.scale(1/1.5), run_time=0.5)

        # Move around the screen
        self.play(triangle.animate.shift(LEFT * 3), run_time=0.5)
        self.play(triangle.animate.shift(RIGHT * 6), run_time=1)
        self.play(triangle.animate.shift(LEFT * 3), run_time=0.5)

        # Create vertex labels
        vertices = triangle.get_vertices()
        labels = VGroup(*[
            Text(label, font_size=24).next_to(vertex, direction)
            for label, vertex, direction in zip(
                ["A", "B", "C"],
                vertices,
                [UP, DOWN + LEFT, DOWN + RIGHT]
            )
        ])

        self.play(FadeIn(labels))
        self.wait(0.5)

        # Transform to different triangle types
        equilateral = RegularPolygon(n=3, color=PURPLE)
        equilateral.set_fill(PURPLE, opacity=0.5)
        equilateral.scale(2)

        self.play(
            Transform(triangle, equilateral),
            FadeOut(labels),
            run_time=1.5
        )
        self.wait(0.5)

        # Final spin and fade out
        self.play(
            Rotate(triangle, angle=2 * TAU),
            triangle.animate.scale(0.1),
            run_time=2
        )
        self.play(FadeOut(triangle))


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


class Rule30Hypergraph(Scene):
    """
    Wolfram Physics style hypergraph evolution using Rule 30.
    Shows 100 steps of foliation with nodes and edges evolving.
    """

    def construct(self):
        # Title
        title = Text("Rule 30 Hypergraph Evolution", font_size=48)
        title.to_edge(UP)
        self.play(Write(title), run_time=1)

        # Rule 30 lookup table: input (left, center, right) -> output
        # Rule 30 in binary: 00011110
        rule30 = {
            (1, 1, 1): 0,
            (1, 1, 0): 0,
            (1, 0, 1): 0,
            (1, 0, 0): 1,
            (0, 1, 1): 1,
            (0, 1, 0): 1,
            (0, 0, 1): 1,
            (0, 0, 0): 0,
        }

        def evolve_rule30(state):
            """Evolve one step using Rule 30."""
            n = len(state)
            new_state = []
            for i in range(n):
                left = state[(i - 1) % n]
                center = state[i]
                right = state[(i + 1) % n]
                new_state.append(rule30[(left, center, right)])
            return new_state

        # Initialize with single cell
        width = 101  # Odd number for symmetry
        initial_state = [0] * width
        initial_state[width // 2] = 1  # Single 1 in center

        # Generate 100 generations
        num_generations = 100
        generations = [initial_state]
        current = initial_state
        for _ in range(num_generations - 1):
            current = evolve_rule30(current)
            generations.append(current)

        # Visualization parameters
        cell_size = 0.07
        start_y = 2.5

        # Create hypergraph visualization
        # We'll show it as evolving network + cellular automaton pattern

        # First show the CA pattern building up
        subtitle = Text("Cellular Automaton Pattern", font_size=28)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle), run_time=0.5)

        # Draw generations in batches for speed
        all_cells = VGroup()
        batch_size = 10

        for gen_batch in range(0, num_generations, batch_size):
            batch_cells = VGroup()
            for gen_idx in range(gen_batch, min(gen_batch + batch_size, num_generations)):
                gen = generations[gen_idx]
                y = start_y - gen_idx * cell_size

                for i, cell in enumerate(gen):
                    if cell == 1:
                        x = (i - width // 2) * cell_size
                        # Color based on generation (time foliation)
                        hue = (gen_idx / num_generations) * 0.7  # Blue to red
                        color = interpolate_color(BLUE, RED, gen_idx / num_generations)

                        dot = Square(
                            side_length=cell_size * 0.9,
                            fill_opacity=0.8,
                            stroke_width=0,
                        )
                        dot.set_fill(color)
                        dot.move_to([x, y, 0])
                        batch_cells.add(dot)

            all_cells.add(batch_cells)
            self.play(FadeIn(batch_cells), run_time=0.15)

        self.wait(1)

        # Now transform to hypergraph view
        self.play(
            FadeOut(subtitle),
            all_cells.animate.scale(0.5).shift(LEFT * 4 + DOWN * 0.5),
            run_time=1.5
        )

        # Create hypergraph representation
        hypergraph_title = Text("Hypergraph View", font_size=28)
        hypergraph_title.move_to([3, 2.5, 0])
        self.play(FadeIn(hypergraph_title), run_time=0.5)

        # Build hypergraph from Rule 30 connections
        # Nodes represent active cells, edges represent causal connections

        # Sample subset of generations for hypergraph (every 10th)
        sample_gens = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99]

        nodes = VGroup()
        edges = VGroup()
        node_positions = {}

        graph_center = np.array([3, 0, 0])
        radius_scale = 1.8

        for layer_idx, gen_idx in enumerate(sample_gens):
            gen = generations[gen_idx]
            active_cells = [i for i, c in enumerate(gen) if c == 1]

            # Position nodes in circular layers
            layer_radius = 0.3 + layer_idx * 0.18

            for node_idx, cell_pos in enumerate(active_cells[:20]):  # Limit nodes per layer
                angle = (node_idx / max(len(active_cells[:20]), 1)) * TAU
                x = graph_center[0] + layer_radius * np.cos(angle) * radius_scale
                y = graph_center[1] + layer_radius * np.sin(angle) * radius_scale

                color = interpolate_color(BLUE, RED, gen_idx / num_generations)
                node = Dot(point=[x, y, 0], radius=0.05, color=color)
                node.set_fill(color, opacity=0.9)
                nodes.add(node)
                node_positions[(gen_idx, cell_pos)] = np.array([x, y, 0])

        # Create edges between adjacent generations (causal connections)
        for i, gen_idx in enumerate(sample_gens[:-1]):
            next_gen_idx = sample_gens[i + 1]
            gen = generations[gen_idx]
            next_gen = generations[next_gen_idx]

            active_curr = [j for j, c in enumerate(gen) if c == 1][:20]
            active_next = [j for j, c in enumerate(next_gen) if c == 1][:20]

            for curr_cell in active_curr[:10]:
                for next_cell in active_next[:10]:
                    # Connect if they're causally related (within 1 cell distance)
                    if abs(curr_cell - next_cell) <= 1:
                        if (gen_idx, curr_cell) in node_positions and (next_gen_idx, next_cell) in node_positions:
                            start = node_positions[(gen_idx, curr_cell)]
                            end = node_positions[(next_gen_idx, next_cell)]

                            edge = Line(start, end, stroke_width=1, stroke_opacity=0.3)
                            edge.set_color(interpolate_color(BLUE_A, RED_A, gen_idx / num_generations))
                            edges.add(edge)

        # Animate hypergraph creation
        self.play(ShowCreation(edges), run_time=2)
        self.play(FadeIn(nodes), run_time=1)

        # Add generation counter
        gen_label = Text(f"Generations: {num_generations}", font_size=24)
        gen_label.to_corner(DR)
        self.play(FadeIn(gen_label), run_time=0.5)

        # Rotate hypergraph for visual effect
        self.play(
            Rotate(VGroup(nodes, edges), angle=TAU, about_point=graph_center),
            run_time=4
        )

        # Final stats
        stats = VGroup(
            Text(f"Total Generations: {num_generations}", font_size=20),
            Text(f"Active Cells (final): {sum(generations[-1])}", font_size=20),
            Text("Rule: 30 (Wolfram)", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT)
        stats.to_corner(DL)

        self.play(FadeIn(stats), run_time=1)
        self.wait(2)

        # Fade out
        self.play(
            FadeOut(VGroup(all_cells, nodes, edges, title, hypergraph_title, gen_label, stats)),
            run_time=1.5
        )
