import random
import matplotlib.pyplot as plt

def tanh(x):
    return (2 / (1 + pow(2.718, -2*x))) - 1

w1 = random.uniform(-0.5, 0.5)  
w2 = random.uniform(-0.5, 0.5)  
w3 = random.uniform(-0.5, 0.5)  
w4 = random.uniform(-0.5, 0.5)  
w5 = random.uniform(-0.5, 0.5)  
w6 = random.uniform(-0.5, 0.5)  
w7 = random.uniform(-0.5, 0.5)  
w8 = random.uniform(-0.5, 0.5)  

b1 = 0.5
b2 = 0.7
i1 = 0.05
i2 = 0.1

net_h1 = (w1 * i1) + (w2 * i2)  + b1
net_h2 = (w3 * i1) + (w4 * i2) + b1
out_h1 = tanh(net_h1)
out_h2 = tanh(net_h2)

net_o1 = (w5 * out_h1) + (w6 * out_h2) + b2
net_o2 = (w7 * out_h1) + (w8 * out_h2) + b2
out_o1 = tanh(net_o1)
out_o2 = tanh(net_o2)

print(f"Output : o1 = {out_o1}, o2 = {out_o2}")

target = [0.1, 0.99]

E_o1 = 0.5 * ((target[0] - out_o1)**2)
print(f"error output 1 : {E_o1}")

E_o2 = 0.5 * ((target[1] - out_o2)**2)
print(f"error output 2 : {E_o2}")

E_total = E_o1 + E_o2
print(f"Total Error : {E_total}")

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

input_layer = [(-0.8, 0.5), (-0.8, -0.5)]
hidden_layer = [(-0.2, 0.5), (-0.2, -0.5)]
output_layer = [(0.4, 0.5), (0.4, -0.5)]

def draw_nodes(layer, label, color):
    for i, (x, y) in enumerate(layer):
        ax.add_patch(plt.Circle((x, y), 0.05, color=color, fill=True))
        ax.text(x - 0.1 if label != 'Output' else x + 0.05, y, f'{label} {i+1}' if label != 'Output' else label, fontsize=10, color='black')

draw_nodes(input_layer, 'Input', 'blue')
draw_nodes(hidden_layer, 'Hidden', 'blue')
draw_nodes(output_layer, 'Output', 'blue')

for i in range(2):
    for j in range(2):
        ax.plot([input_layer[i][0], hidden_layer[j][0]], [input_layer[i][1], hidden_layer[j][1]], 'k-', lw=1)
for j in range(2):
    for k in range(2):
        ax.plot([hidden_layer[j][0], output_layer[k][0]], [hidden_layer[j][1], output_layer[k][1]], 'k-', lw=1)

plt.show()

