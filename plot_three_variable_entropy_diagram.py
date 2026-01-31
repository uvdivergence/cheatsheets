from matplotlib import pyplot as plt
from matplotlib_venn import venn3

plt.figure()

v = venn3(
    subsets = (3, 3, 1, 3, 1, 1, 1),
    set_labels = ('A', 'B',  'C'),
    set_colors=("blue", "red", "yellow"),
    alpha=0.6
)

v.get_label_by_id('100').set_text('$H(X | Y, Z)$')
v.get_label_by_id('001').set_text('$H(Z | X, Y)$')
v.get_label_by_id('010').set_text('$H(Y | X, Z)$')

v.get_label_by_id('011').set_text('$I(Y ,Z | X)$')
v.get_label_by_id('101').set_text('$I(Z, X | Y)$')
v.get_label_by_id('110').set_text('$I(X ,Y | Z)$')


v.get_label_by_id('111').set_text('$I(X, Y, Z)$')

v.get_label_by_id('A').set_text('$H(X)$')
v.get_label_by_id('B').set_text('$H(Y)$')
v.get_label_by_id('C').set_text('$H(Z)$')

plt.title("$H(X, Y, Z)$")
plt.savefig("three_variable_entropy_diagram.jpg")
