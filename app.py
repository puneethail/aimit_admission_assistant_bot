import chainlit as cl
from src.llm import initialize_chat_session, get_response


@cl.on_chat_start
async def start_chat():
    """
    This function is decorated to run when a new chat session starts.
    It initializes the Gemini chat session and stores it in the user's session state.
    """
    try:
        chat_session = initialize_chat_session()
        # to store chat history
        cl.user_session.set("chat_session", chat_session)
        
        await cl.Message(content= '''Hello! 👋 I’m AIMIT Connect. How can I help you today?''').send()
    except KeyError:
        # Handle the case where the API key is not found in environment variables.
        error_message = ("😶‍🌫️ API Key not found.")
        await cl.Message(content=error_message).send()
        
    except ValueError as e:
        # Handle other initialization errors
        error_message = f"An error occurred during initialization: {e}"
        await cl.Message(content=error_message).send()

@cl.on_message
async def main(message: cl.Message):
    """
    This function is decorated to run every time the user sends a message.
    It retrieves the chat session and sends the message to the Gemini model.
    """
    # Retrieve the chat session object from the user's session state.
    chat_session = cl.user_session.get("chat_session")
    
    
    # Check if the chat session was successfully initialized
    if chat_session:
        # Call your backend function to get the response.
        response = get_response(message.content, chat_session)
        # Stream the tokens to the message in the UI
        if isinstance(response, str):
            await cl.Message(content=response).send()
        else:
            # Create a new message to hold the streaming response
            msg = cl.Message(content="")
            await msg.send()
            
            # Stream the tokens to the message in the UI
            for token in response:
                await msg.stream_token(token.text)
            
            # Send the final message to mark the stream as complete
            await msg.send()
    else:
        msg = cl.Message(content="")
        await msg.send()
        # If the session couldn't be initialized, inform the user.
        response = "I'm sorry, the chat session was not properly initialized. Please restart the chat."
        for token in response:
                await msg.stream_token(token.text)
        await msg.send()

