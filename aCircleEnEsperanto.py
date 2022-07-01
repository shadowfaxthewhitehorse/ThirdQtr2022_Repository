# PYTHON CODE
#
# :ENGLISH:
#
# Do you want to see how the various mathematical attributes of a circle can be succincely captured in code? If so, read below.
# 
# :ESPERANTO:
#
# Ĉu vi volas vidi kiel la diversaj matematikaj atributoj de cirklo povas esti koncize kaptitaj en kodo? Se jes, legu sube.
#
import math

class aCircle:
    radius = 0.0

    def setRadius(self, inRadius):
    	self.radius = inRadius
    	return

    def area(self):
    	return(math.pi * self.radius * self.radius)

    def circumference(self):
        return(2 * math.pi * self.radius)


n1Circle = aCircle()

n1Circle.setRadius(5)

print("The area of the circle is :", n1Circle.area())
