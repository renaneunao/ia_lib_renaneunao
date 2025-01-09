def autoplay_audio(file_path: str, placeholder, autoplay):
    import base64
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()

    # Construindo a tag <audio> com base no valor de autoplay
    autoplay_attr = "autoplay" if autoplay else ""

    md = f"""
    <audio controls {autoplay_attr}>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """

    placeholder.markdown(md, unsafe_allow_html=True)

def gerar_audio(st, model, voice, resposta_obtida, autoplay):
    audio_file_path = "output.mp3"
    try:
        # Create a placeholder for the audio player
        audio_placeholder = st.empty()
        # Check if the audio has already been generated
        if st.session_state.audio_generated:
            autoplay_audio(audio_file_path, audio_placeholder, autoplay=False)
            return
        else:
            with st.spinner('Gerando áudio...'):
                response = get_client_openai().audio.speech.create(
                    model=model,
                    voice=voice,
                    input=resposta_obtida
                )
                response.write_to_file(audio_file_path)

                # Clear any previous audio player
                audio_placeholder.empty()
                # Autoplay the generated audio
                autoplay_audio(audio_file_path, audio_placeholder, autoplay=autoplay)

                st.session_state.audio_generated = True
    except Exception as e:
        st.error(f"Ocorreu um erro ao gerar o áudio: {e}")
