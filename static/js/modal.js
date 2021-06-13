function openTab(evt, tabName) {
  var i, tabcontent, tablinks;

  tabcontent = document.getElementsByClassName(
    'betremit-modal-dialog__content-tabcontent'
  );
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = 'none';
  }

  tablinks = document.getElementsByClassName(
    'betremit-modal-dialog__navigation-item'
  );
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(' active', '');
  }

  document.getElementById(tabName).style.display = 'block';
  evt.currentTarget.className += ' active';
}

function closeModal() {
  window.top.closeIframe();
}

function initialLoader() {
  var initialLoad = document.querySelector('.loading-dots__initial');
  var mainContent = document.querySelector('.betremit-modal-dialog__container');
  setTimeout(() => {
    initialLoad.style.display = 'none';
    mainContent.style.display = 'block';
  }, 1000);
}

function copyText(evt) {
  var copyText = document.getElementById(evt.currentTarget.id);
  copyText.select();
  document.execCommand('copy');
}

function displayLoader(loader, formParent) {
  loader.style.display = 'block';
  formParent.style.display = 'none';
  setTimeout(() => {
    loader.style.display = 'none';
    formParent.style.display = 'block';
  }, 1000);
}

function displaySuccess(successSection, formParent) {
  new Vivus('success-svg', { duration: 20 });
  successSection.style.display = 'block';
  formParent.style.display = 'none';
  setTimeout(() => {
    successSection.style.display = 'none';
    formParent.style.display = 'block';
  }, 1000);
}

function displayError(errorSection, formParent) {
  new Vivus('error-svg', { duration: 30 });
  errorSection.style.display = 'block';
  formParent.style.display = 'none';
  setTimeout(() => {
    errorSection.style.display = 'none';
    formParent.style.display = 'block';
  }, 1000);
}

function submitForm(evt, loaderName) {
  evt.preventDefault();
  var loader = document.getElementById(loaderName);
  var form = evt.currentTarget;
  var formParent = form.parentNode.parentNode;
  var successSection =
    form.parentNode.parentNode.nextSibling.nextSibling.nextSibling.nextSibling;
  var errorSection =
    form.parentNode.parentNode.nextSibling.nextSibling.nextSibling.nextSibling
      .nextSibling.nextSibling;
  displayLoader(loader, formParent);
  setTimeout(() => {
    // displaySuccess(successSection, formParent);
    displayError(errorSection, formParent);
  }, 1000);
  form.reset();
  evt.currentTarget.submitButton.disabled = true;
}

function disableSubmit(evt) {
  var documentForms = document.forms;
  for (i = 0; i < documentForms.length; i++) {
    documentForms[i].submitButton.disabled = true;
  }
}

function isDisabled(currentValue) {
  return Boolean(currentValue) === true;
}

function getFormValuesArray(formElements) {
  var formValuesArray = [];
  for (i = 0; i < formElements.length - 1; i++) {
    formValuesArray[i] = formElements[i].value;
  }
  return formValuesArray;
}

function validateForm(evt) {
  var formName = evt.currentTarget.name;
  var formElements = document.forms[formName].elements;
  var formValuesArray = getFormValuesArray(formElements);
  if (formValuesArray.every(isDisabled)) {
    formElements.submitButton.disabled = false;
  }
}

initialLoader();

disableSubmit();
