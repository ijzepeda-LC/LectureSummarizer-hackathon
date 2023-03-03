import streamlit as st
import streamlit_webrtc as webrtc

def app():
    st.title("WebRTC Audio Recorder")

    webrtc_ctx = webrtc.StreamerRTC(audio=True, key="audio")

    if not webrtc_ctx:
        st.warning("No audio devices found.")
        return

    if st.button("Start Recording"):
        webrtc_ctx.start_recording()
        st.info("Recording started.")

    if st.button("Stop Recording"):
        webrtc_ctx.stop_recording()
        st.success("Recording stopped.")

    if webrtc_ctx.audio_receiver:
        st.audio(webrtc_ctx.audio_receiver.get_audio(), format='audio/wav')

if __name__ == "__main__":
    app()
import streamlit as st
import streamlit_webrtc as webrtc

def app():
    st.title("WebRTC Audio Recorder")

    webrtc_ctx = webrtc.StreamerRTC(audio=True, key="audio")

    if not webrtc_ctx:
        st.warning("No audio devices found.")
        return

    if st.button("Start Recording"):
        webrtc_ctx.start_recording()
        st.info("Recording started.")

    if st.button("Stop Recording"):
        webrtc_ctx.stop_recording()
        st.success("Recording stopped.")

    if webrtc_ctx.audio_receiver:
        st.audio(webrtc_ctx.audio_receiver.get_audio(), format='audio/wav')

if __name__ == "__main__":
    app()
