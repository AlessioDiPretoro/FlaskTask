function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/notes";
  });
}

function editNote(note) {
  fetch("/edit-note", {
    method: "POST",
    body: JSON.stringify({ note: note }),
  }).then((_res) => {
    window.location.href = "/notes";
  });
}
