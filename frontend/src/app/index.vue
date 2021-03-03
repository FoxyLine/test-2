<template>
<div :class="'app'">
	<KanbanBoard></KanbanBoard>
</div>
</template>

<script>
import { KanbanBoard } from './components';
export default {
	name: "App",
	components: {
		KanbanBoard
	} 
};
</script>

<style src="../style.css"/>

