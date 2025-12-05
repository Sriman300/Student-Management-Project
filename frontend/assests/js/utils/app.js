import { initStudentController } from "./controllers/studentController.js";
import { router } from "./router/viewRouter.js";
window.addEventListener("DOMContentLoaded", () => {
  router();
  initStudentController();


});