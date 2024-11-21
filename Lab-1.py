import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

state = {
    'time_of_day' : 'night',
    'temperature' : 28,
    'people_present' : False,
    'doors_locked' : False,
    'lights_on' : False,
    'AC_on' : False
}

# Define the function to apply rules
def apply_rules (state):
    #Rule 1: Turn on Lights in the evening if someone is home 
    if state['time_of_day'] == 'night' and not state['lights_on']:
        state['lights_on'] = True

    # Rule 2: Adjust thermostat if it's cold and someone is home 
    if state['temperature']> 25:
        state['AC_on'] = True

    #Rule 3: Lock doors if no one is home 
    if not state['people_present'] and not state['doors_locked']:
        state['doors_locked'] = True

    return state

# Function to visualize the smart home state as a  dashboard grid
def visualize_state_grid(state, title="Smart Home State"):

    #Set up the plot
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0 , 3)
    ax.set_ylim(0, len(state))
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.axis("off")

    # Define colors for each state based on device type
    color_map = {
        "locked": "green", "unlocked": "yellow", 
        True: "green", False: "yellow", 
        "night": "aqua", "evening": "aqua", 
        "temperature": "green"
    }

    # Place each device state as a colored rectangle in the grid 
    for i, (device, state) in enumerate (state.items()):
        color = color_map.get(state, "green") # Define color

        ## https://chatgpt.com/share/67370362-e380-8000-a300-99ed427c352a (Explaination)
        #Drawing rectangle and adding text
        rect = Rectangle((0.5, i), 2, 1, color = color, edgecolor="black")   
        ax.add_patch(rect)

        #Add device name and state text
        ax.text(1, i+0.5, device.capitalize(), va="center", ha="center", fontweight="bold", color="black")
        ax.text(2, i + 0.5, str(state), va="center", ha="center", fontweight="bold", color="black")

    plt.show()


print("initial state", state)
visualize_state_grid(state, title="Initial Smart Home State")

apply_rules(state)
print("final state", state)
visualize_state_grid(state, title="Smart Home State")