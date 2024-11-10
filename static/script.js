// document.getElementById('convertForm').addEventListener('submit', function(event) {
//     event.preventDefault();
    
//     var formData = new FormData();
//     var fileInput = document.getElementById('fileInput');
    
//     if (fileInput.files.length > 0) {
//         formData.append('file', fileInput.files[0]);

//         // إرسال الملف إلى الخادم
//         fetch('/convert_file_to_audio', {
//             method: 'POST',
//             body: formData
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.audio_file) {
//                 var downloadLink = document.getElementById('downloadLink');
//                 downloadLink.href = '/uploads/' + data.audio_file;  // تحديد رابط الملف الصوتي
//                 document.getElementById('downloadSection').style.display = 'block';  // إظهار قسم التحميل
//             } else {
//                 alert('Error converting file to audio.');
//             }
//         })
//         .catch(error => {
//             console.error('Error:', error);
//             alert('Error during conversion');
//         });
//     }
// });
