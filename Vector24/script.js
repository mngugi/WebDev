// Initialize date
const date = new Date();

const renderCalendar = () => {
    date.setDate(1);

    const monthDays = document.querySelector(".calendar-dates");
    const currentDate = document.querySelector(".calendar-current-date");

    const lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();
    const prevLastDay = new Date(date.getFullYear(), date.getMonth(), 0).getDate();

    const firstDayIndex = date.getDay();
    const lastDayIndex = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDay();

    const nextDays = 7 - lastDayIndex - 1;

    const months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];

    currentDate.innerHTML = `${months[date.getMonth()]} ${date.getFullYear()}`;

    let days = "";

    // Previous month's days
    for (let x = firstDayIndex; x > 0; x--) {
        days += `<li class="prev-date">${prevLastDay - x + 1}</li>`;
    }

    // Current month's days
    for (let i = 1; i <= lastDay; i++) {
        if (i === new Date().getDate() && date.getMonth() === new Date().getMonth()) {
            days += `<li class="today">${i}</li>`;
        } else {
            days += `<li>${i}</li>`;
        }
    }

    // Next month's days
    for (let j = 1; j <= nextDays; j++) {
        days += `<li class="next-date">${j}</li>`;
    }

    monthDays.innerHTML = days;
};

document.querySelector("#calendar-prev").addEventListener("click", () => {
    date.setMonth(date.getMonth() - 1);
    renderCalendar();
});

document.querySelector("#calendar-next").addEventListener("click", () => {
    date.setMonth(date.getMonth() + 1);
    renderCalendar();
});

renderCalendar();
