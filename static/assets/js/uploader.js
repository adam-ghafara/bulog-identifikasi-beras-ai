const dropzone = document.getElementById('dropzone');
const dropzoneInput = document.getElementById('dropzone-file');
const preview = document.getElementById('preview');
const previewImage = document.getElementById('preview-image');
const uploadText = document.getElementById('upload-text');
const icon = document.getElementById('icon');

function handleFileUpload(file) {
    if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            previewImage.src = e.target.result;
            preview.classList.remove('hidden');
            uploadText.textContent = file.name;
            icon.classList.add('hidden');
        };
        reader.readAsDataURL(file);
    }
}

dropzoneInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    handleFileUpload(file);
});

dropzone.addEventListener('dragover', (event) => {
    event.preventDefault();
});

dropzone.addEventListener('drop', (event) => {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    handleFileUpload(file);
    dropzoneInput.files = event.dataTransfer.files;
});