<template>
    <div class="relative inline-block" ref="dropdownContainer">
        <button @click="toggleDropdown" id="dropdownDefaultButton"
            class="dark:bg-gray-900 text-white hover:bg-white hover:text-black focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center inline-flex items-center"
            type="button">
            Filter
            <svg class="w-2.5 h-2.5 ms-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                viewBox="0 0 10 6">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="m1 1 4 4 4-4" />
            </svg>
        </button>

        <div :class="{ block: isDropdownVisible, hidden: !isDropdownVisible }" id="dropdownDefaultCheckbox"
            class="z-50 absolute top-full mt-2 w-48 divide-y divide-gray-100 rounded-lg shadow dark:bg-gray-900 m-2">
            <ul class="p-3 space-y-3 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownCheckboxButton">
                <li>
                    <div class="flex items-center">
                        <input id="radio-item-1" name="filter" type="radio" value="price"
                            class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                        <label for="radio-item-1" class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                            Price
                        </label>
                    </div>
                </li>
                <li>
                    <div class="flex items-center">
                        <input id="radio-item-2" name="filter" type="radio" value="ratings"
                            class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                        <label for="radio-item-2" class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                            Ratings
                        </label>
                    </div>
                </li>
                <li>
                    <div class="flex items-center">
                        <input id="radio-item-3" name="filter" type="radio" value="new-listings"
                            class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" />
                        <label for="radio-item-3" class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                            New Listings
                        </label>
                    </div>
                </li>
            </ul>
        </div>

    </div>
</template>

<script>
export default {
    data() {
        return {
            isDropdownVisible: false,
        };
    },
    methods: {
        toggleDropdown() {
            this.isDropdownVisible = !this.isDropdownVisible;
        },
        handleClickOutside(event) {
            if (this.$refs.dropdownContainer && !this.$refs.dropdownContainer.contains(event.target)) {
                this.isDropdownVisible = false;
            }
        },
    },

    mounted() {
        document.addEventListener('click', this.handleClickOutside);
    },
    beforeDestroy() {
        document.removeEventListener('click', this.handleClickOutside);
    },
};
</script>
