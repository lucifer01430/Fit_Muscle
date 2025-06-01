document.addEventListener('DOMContentLoaded', function () {
    // Existing validation code...
    // Appointment Form Validation
    const appointmentForm = document.querySelector('.form_start');
    if (appointmentForm) {
        appointmentForm.addEventListener('submit', function (e) {
            let hasError = false;
            const errorStyle = 'color: red; font-size: 0.9em; margin-top: 5px;';

            // Clear previous error messages
            const existingErrors = appointmentForm.querySelectorAll('.error-message');
            existingErrors.forEach(error => error.remove());

            // Full Name
            const fullName = appointmentForm.querySelector('input[name="full_name"]').value.trim();
            const nameRegex = /^[a-zA-Z\s]+$/;
            if (!fullName) {
                hasError = true;
                const error = document.createElement('div');
                error.className = 'error-message';
                error.style.cssText = errorStyle;
                error.textContent = 'Full name is required.';
                appointmentForm.querySelector('input[name="full_name"]').after(error);
            } else if (!nameRegex.test(fullName)) {
                hasError = true;
                const error = document.createElement('div');
                error.className = 'error-message';
                error.style.cssText = errorStyle;
                error.textContent = 'Full name can only contain letters and spaces.';
                appointmentForm.querySelector('input[name="full_name"]').after(error);
            }

            // Phone Number
            const phoneNumber = appointmentForm.querySelector('input[name="phone_number"]').value.trim();
            const phoneRegex = /^\+?\d{10,15}$/;
            if (!phoneNumber) {
                hasError = true;
                const error = document.createElement('div');
                error.className = 'error-message';
                error.style.cssText = errorStyle;
                error.textContent = 'Phone number is required.';
                appointmentForm.querySelector('input[name="phone_number"]').after(error);
            } else if (!phoneRegex.test(phoneNumber)) {
                hasError = true;
                const error = document.createElement('div');
                error.className = 'error-message';
                error.style.cssText = errorStyle;
                error.textContent = 'Please enter a valid phone number (10-15 digits, optionally starting with +).';
                appointmentForm.querySelector('input[name="phone_number"]').after(error);
            }

            // Email
            const email = appointmentForm.querySelector('input[name="email"]').value.trim();
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!email) {
                hasError = true;
                const error = document.createElement('div');
                error.className = 'error-message';
                error.style.cssText = errorStyle;
                error.textContent = 'Email address is required.';
                appointmentForm.querySelector('input[name="email"]').after(error);
            } else if (!emailRegex.test(email)) {
                hasError = true;
                const error = document.createElement('div');
                error.className = 'error-message';
                error.style.cssText = errorStyle;
                error.textContent = 'Please enter a valid email address.';
                appointmentForm.querySelector('input[name="email"]').after(error);
            }

            // Message (optional, but check length if provided)
            const message = appointmentForm.querySelector('textarea[name="message"]').value.trim();
            if (message.length > 500) {
                hasError = true;
                const error = document.createElement('div');
                error.className = 'error-message';
                error.style.cssText = errorStyle;
                error.textContent = 'Message cannot exceed 500 characters.';
                appointmentForm.querySelector('textarea[name="message"]').after(error);
            }

            if (hasError) {
                e.preventDefault();  // Prevent form submission if there are errors
            }
        });
    }

    // Subscription Form Validation
    const subscriptionForm = document.querySelector('.footer_subscribe_box');
    if (subscriptionForm) {
        subscriptionForm.addEventListener('submit', function (e) {
            let hasError = false;
            const errorStyle = 'color: red; font-size: 0.9em; margin-top: 5px;';

            // Clear previous error messages
            const existingErrors = subscriptionForm.querySelectorAll('.error-message');
            existingErrors.forEach(error => error.remove());

            // Email
            const email = subscriptionForm.querySelector('input[name="email"]').value.trim();
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!email) {
                hasError = true;
                const error = document.createElement('div');
                error.className = 'error-message';
                error.style.cssText = errorStyle;
                error.textContent = 'Email address is required.';
                subscriptionForm.querySelector('input[name="email"]').after(error);
            } else if (!emailRegex.test(email)) {
                hasError = true;
                const error = document.createElement('div');
                error.className = 'error-message';
                error.style.cssText = errorStyle;
                error.textContent = 'Please enter a valid email address.';
                subscriptionForm.querySelector('input[name="email"]').after(error);
            }

            if (hasError) {
                e.preventDefault();  // Prevent form submission if there are errors
            }
        });
    }

    // Fade out success messages after 5 seconds
    const successMessages = document.querySelectorAll('.alert.alert-success');
    successMessages.forEach(message => {
        setTimeout(() => {
            message.style.transition = 'opacity 1s';
            message.style.opacity = '0';
            setTimeout(() => message.remove(), 1000);
        }, 5000);
    });
});