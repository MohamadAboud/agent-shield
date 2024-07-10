// Change the icons to the ones you want to use.

// JavaScript code to change the favicon
function changeFavicon(iconURL) {
    // Find existing favicon elements
    let link = document.querySelector("link[rel*='icon']") || document.createElement('link');
    link.type = 'image/x-icon';
    link.rel = 'shortcut icon';
    link.href = iconURL;

    // Remove any existing favicons
    const existingIcons = document.querySelectorAll("link[rel*='icon']");
    existingIcons.forEach(icon => icon.parentNode.removeChild(icon));

    // Append the new favicon
    document.getElementsByTagName('head')[0].appendChild(link);
}

// Example usage:
changeFavicon("public/logo.svg");