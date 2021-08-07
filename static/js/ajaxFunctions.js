document
  .getElementById("updateGrocery")
  .addEventListener("submit", updateGrocery);

function updateGrocery(e) {
  e.preventDefault();

  Swal.fire({
    title: "Do you want to update the changes?",
    showDenyButton: true,
    showCancelButton: true,
    confirmButtonText: `Update`,
    denyButtonText: `Don't update`,
  }).then((result) => {
    if (result.isConfirmed) {
      const formData = new FormData(this);

      fetch("http://localhost:8000/update/", {
        method: "post",
        body: formData,
      })
        .then((response) => response.text())
        .then((text) => {
          if (text === "ok") {
            Swal.fire("Updated!", "", "success").then((el) =>
              window.location.replace("http://localhost:8000/")
            );
          } else {
            Swal.fire("Something happend while updating", "", "error");
          }
        });
    } else if (result.isDenied) {
      Swal.fire("Changes are not saved", "", "info");
    }
  });
}
