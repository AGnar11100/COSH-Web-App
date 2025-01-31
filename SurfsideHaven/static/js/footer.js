document.addEventListener("DOMContentLoaded", function () {
    const footer = document.querySelector("footer");
    const body = document.body;
    
    function adjustFooterPosition() {
        const contentHeight = body.scrollHeight; // Total content height
        const viewportHeight = window.innerHeight; // Viewport height

        if (contentHeight > viewportHeight) {
            // If content exceeds viewport height, allow normal scrolling
            footer.style.position = "relative";
        } else {
            // If content is too short, stick footer to bottom
            footer.style.position = "absolute";
            footer.style.bottom = "0";
            footer.style.width = "100%";
        }
    }

    adjustFooterPosition();
    window.addEventListener("resize", adjustFooterPosition);
});
