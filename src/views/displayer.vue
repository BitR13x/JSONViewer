<script lang="ts">
export default {
    data() {
        return {
            file: null as File | null,
            data: [{ name: "", href: "", open: false }]
        }
    },
    methods: {
        handleFileChange(event: any): void {
            this.file = event.target.files[0];
        },
        handleUpload(): void {
            if (!this.file) {
                console.log("Please select a file to upload.")
                return;
            }
            const reader = new FileReader();
            reader.onload = () => {
                let text = reader.result;
                if (typeof (text) !== null) {
                    this.data = JSON.parse(text as string)
                }

            }
            reader.readAsText(this.file);
        },
        toggleOpen(id: Number) {
            this.data.forEach((item, index) => {
                if (index === id) {
                    item.open = !item.open;
                } else {
                    item.open = false;
                }
            });
        }
    }
};
</script>

<template>
    <div class="main">
        <div class="uploadForm">
            <input type="file" ref="fileInput" @change="handleFileChange" />
            <button @click="handleUpload">Upload</button>
        </div>
        <div class="list-names">
            <ul v-if="data[0].name">
                <li v-for="(item, index) in data" :key="index">
                    <div class="Name" @click="toggleOpen(index)">
                        {{ item.name }}
                    </div>
                    <transition class="Content" name="slide">
                        <div v-if="item.open" class="content">
                            <a v-bind:href="item.href" target="_blank">{{ item.href }}</a>
                        </div>
                    </transition>
                </li>
            </ul>
        </div>
    </div>
</template>

<style scoped>
.main {
    margin-top: 10rem;
}

.uploadForm {
    padding-left: 5vw;
}

.content {
    margin-left: 4vw;
}

.Name {
    font-size: 2vw;
}

.Name:hover {
    background-color: rgba(84, 84, 84, 0.65);
    transition: 0.4s;
}

.active {
    background-color: rgb(0, 55, 37);
}

.TypeButtons {
    margin-top: 2rem;
    margin-bottom: 2rem;
    padding-left: 5vw;
}

button,
input {
    background-color: rgb(3, 119, 80);
    border-radius: 1rem;
    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    /* Green */
    border: none;
    color: white;
    margin-right: 1rem;
    padding: 7.5px 16px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
}

button:hover {
    box-shadow: 0 12px 16px 0 rgba(0, 0, 0, 0.24), 0 17px 50px 0 rgba(0, 0, 0, 0.19);
    background-color: rgb(0, 55, 37);
}

.list-names {
    padding-left: 1vw;
    text-align: left;
}

.slide-enter-active,
.slide-leave-active {
    transition: all 0.3s ease;
}

.slide-enter,
.slide-leave-to {
    transform: translateY(-100%);
}
</style>
