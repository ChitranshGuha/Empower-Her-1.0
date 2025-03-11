from flask_socketio import emit

@socketio.on('userType')
def handle_user_type(user_type):
    # Handle agent and customer connections
    # Maintain lists of connected agents and customers
    ...

@socketio.on('customerMessage')
def handle_customer_message(message):
    # Broadcast to all agents
    ...

@socketio.on('agentMessage')
def handle_agent_message(message):
    # Broadcast to all customers
    ...
