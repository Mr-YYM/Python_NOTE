def main():
    txtDiagram = create_diagram(DiagramFactory())
    txtDiagram.save(textFilename)

    svgDiagram = create_diagram(SvggramFactory())
    svgDiagram.save(svgFilename)
