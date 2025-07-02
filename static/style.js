const fileInput = document.getElementById('fileUpload');
const preview = document.querySelector('.preview-img');
const previewBox = document.getElementById('imagePreview');
const previewText = previewBox.querySelector('p');

fileInput.addEventListener('change', function () {
  const file = this.files[0];
  if (file) {
    const reader = new FileReader();

    preview.style.display = 'block';
    previewText.style.display = 'none';

    reader.addEventListener('load', function () {
      preview.setAttribute('src', this.result);
    });

    reader.readAsDataURL(file);
  } else {
    preview.setAttribute('src', '');
    preview.style.display = 'none';
    previewText.style.display = 'block';
  }
});
