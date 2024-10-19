onload = () => {
  const timeout = setTimeout(() => {
    document.body.classList.remove("not-loaded");
    clearTimeout(timeout);

    // Tự động cuộn xuống dòng chữ chúc sau khi hoa nở
    const messageElement = document.querySelector('.message');
    setTimeout(() => {
      messageElement.scrollIntoView({ behavior: 'smooth' });
    }, 4000); // 4 giây delay để hoa nở xong
  }, 1000);
};
