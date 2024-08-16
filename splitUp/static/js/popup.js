const modal = document.createElement('div');
modal.id = 'myModal';
modal.innerHTML = ` 
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close-button" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <p>Your payment is due till the date <span id="dueDate"></span></p>
      </div>
      <div class="modal-footer">
          <button type="button" class="due_button">Due the Payment</button>
      </div>
    </div>
  </div>
`;

document.body.appendChild(modal); 

const style = document.createElement('style');
style.innerHTML = `
  #myModal {
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.4);
  }
  .modal-dialog {
    position: relative;
    margin: 10% auto;
    max-width: 500px;
  }
  .modal-content {
    background-color: #fefefe;
    margin: 15% auto;
    padding: 20px;
    border: 1px solid #888;
    width: 100%;
    height: auto;
    max-width: 500px;
    border-radius: 10px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    }

  .modal-header {
    padding-bottom:20px;
    }
  
    .modal-body {
  padding-bottom:15px;
  }

  .close-button {
    color: #aaa;
    float: right;
    font-size: 23px;
    font-weight: bold;
    cursor: pointer;
    border: none;
    background:none;
  }

  .close-button:hover {
    color: #000;
    text-decoration: none;
  }
  
  .modal-footer {
    padding-bottom:20px;
  }

  .due_button {
    float: right;
    font-size: 15px;
    cursor: pointer;
  }
`;

document.head.appendChild(style);

function formatDate(date) {
  var day = String(date.getDate()).padStart(2, '0'); 
  var month = String(date.getMonth() + 1).padStart(2, '0'); 
  var year = date.getFullYear(); 
  return `${day}/${month}/${year}`;
}

function ShowModal() {
  const currentDate = new Date();
  let dueDate = new Date();   // have to fetch from project table
  dueDate.setDate(dueDate.getDate() + 2);


  const dueDateSpan = document.getElementById('dueDate');
  if (dueDateSpan) {
    dueDateSpan.textContent = formatDate(dueDate);
  }

  // modal.style.display = 'block';

  const closeButton = document.querySelector('.close-button');
  closeButton.onclick = () => {
    modal.style.display = 'none';
  };

}
window.onload = ShowModal;
