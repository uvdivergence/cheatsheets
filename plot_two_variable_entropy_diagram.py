from matplotlib import pyplot as plt
from matplotlib_venn import venn2

plt.figure()

v = venn2(
    subsets = (2, 2, 1),
    set_labels = ('A', 'B'),
    set_colors=("blue", "red"),
    alpha=0.6
)

v.get_label_by_id('10').set_text('$H(X|Y)$')
v.get_label_by_id('01').set_text('$H(Y|X)$')
v.get_label_by_id('11').set_text('$I(X, Y)$')
v.get_label_by_id('A').set_text('$H(X)$')
v.get_label_by_id('B').set_text('$H(Y)$')

plt.title("$H(X, Y)$")
plt.savefig("two_variable_entropy_diagram.jpg")