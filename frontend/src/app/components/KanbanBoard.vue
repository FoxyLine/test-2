<template>
	<div v-if="token" class="kanban-board">
		<div class="row">
			<h3 class="header orange">On Hold ({{RED.length}})</h3>
			<Container :group-name="'1'" :get-child-payload="getChildPayload0" @drop="onDrop('RED', $event)">
				<Draggable v-for="item in RED" :key="item.id">
					<div class="draggable-item">
						<div class="delete" @click="deleteItem('RED', item)"></div>
						<p><b class="id">id: </b>{{item.id}}</p>
						<p class="card-text">{{item.text}}</p>
						<p class="card-time">created: {{item.create_date}}</p>
						<p class="card-time">updated: {{item.update_date}}</p>
					</div>
				</Draggable>
			</Container>
			<textarea id="title0" class="card-title-textarea" rows="5" placeholder="Ввести заголовок для этой карточки" v-model="newCardText" v-bind:style="addACardStyle[0]"></textarea>
			<button class="add-a-card" @click="addItem('RED')" v-bind:style="addACardStyle[0]">Добавить карточку</button>
			<button class="cancel" @click="hideAddACardTextarea()" v-bind:style="addACardStyle[0]"></button>
			<button class="add-another-card" @click="showAddACardTextarea(0)" v-bind:style="addAnotherCardStyle[0]">Добавить карточку</button>
		</div>
		<div class="row">
			<h3 class="header blue">In Progress ({{BLUE.length}})</h3>
			<Container :group-name="'1'" :get-child-payload="getChildPayload1" @drop="onDrop('BLUE', $event)">
				<Draggable v-for="item in BLUE" :key="item.id">
					<div class="draggable-item">
						<div class="delete" @click="deleteItem('BLUE', item)"></div>
						<p><b class="id">id: </b>{{item.id}}</p>
						<p class="card-text">{{item.text}}</p>
						<p class="card-time">created: {{item.create_date}}</p>
						<p class="card-time">updated: {{item.update_date}}</p>						
					</div>
				</Draggable>
			</Container>
			<textarea id="title1" class="card-title-textarea" rows="5" placeholder="Ввести заголовок для этой карточки" v-model="newCardText" v-bind:style="addACardStyle[1]"></textarea>
			<button class="add-a-card" @click="addItem('BLUE')" v-bind:style="addACardStyle[1]">Добавить карточку</button>
			<button class="cancel" @click="hideAddACardTextarea()" v-bind:style="addACardStyle[1]"></button>
			<button class="add-another-card" @click="showAddACardTextarea(1)" v-bind:style="addAnotherCardStyle[1]">Добавить карточку</button>
		</div>
		<div class="row">
			<h3 class="header yellow">Needs Review ({{YELLOW.length}})</h3>
			<Container :group-name="'1'" :get-child-payload="getChildPayload2" @drop="onDrop('YELLOW', $event)"> 
				<Draggable v-for="item in YELLOW" :key="item.id">
					<div class="draggable-item">
						<div class="delete" @click="deleteItem('YELLOW', item)"></div>
						<p><b class="id">id: </b>{{item.id}}</p>
						<p class="card-text">{{item.text}}</p>
						<p class="card-time">created: {{item.create_date}}</p>
						<p class="card-time">updated: {{item.update_date}}</p>						
					</div>
				</Draggable>
			</Container>
			<textarea id="title2" class="card-title-textarea" rows="5" placeholder="Ввести заголовок для этой карточки" v-model="newCardText" v-bind:style="addACardStyle[2]"></textarea>
			<button class="add-a-card" @click="addItem('YELLOW')" v-bind:style="addACardStyle[2]">Добавить карточку</button>
			<button class="cancel" @click="hideAddACardTextarea()" v-bind:style="addACardStyle[2]"></button>
			<button class="add-another-card" @click="showAddACardTextarea(2)" v-bind:style="addAnotherCardStyle[2]">Добавить карточку</button>
		</div>
		<div class="row">
			<h3 class="header green">Approved ({{GREEN.length}})</h3>
			<Container :group-name="'1'" :get-child-payload="getChildPayload3" @drop="onDrop('GREEN', $event)">
				<Draggable v-for="item in GREEN" :key="item.id">
					<div class="draggable-item">
						<div class="delete" @click="deleteItem('GREEN', item)"></div>
						<p><b class="id">id: </b>{{item.id}}</p>
						<p class="card-text">{{item.text}}</p>
						<p class="card-time">created: {{item.create_date}}</p>
						<p class="card-time">updated: {{item.update_date}}</p>						
					</div>
				</Draggable>
			</Container>
			<textarea id="title3" class="card-title-textarea" rows="5" placeholder="Ввести заголовок для этой карточки" v-model="newCardText" v-bind:style="addACardStyle[3]"></textarea>
			<button class="add-a-card" @click="addItem('GREEN')" v-bind:style="addACardStyle[3]">Добавить карточку</button>
			<button class="cancel" @click="hideAddACardTextarea()" v-bind:style="addACardStyle[3]"></button>
			<button class="add-another-card" @click="showAddACardTextarea(3)" v-bind:style="addAnotherCardStyle[3]">Добавить карточку</button>
		</div>
	</div>
	<div v-else >
		<p class="no-auth"><a href='accounts/signup/'>signup</a> or <a href='signin'>signin</a> before using kanban</p>
	</div>
</template>

<script>
import { Container, Draggable } from "vue-smooth-dnd";
import { applyDrag, loadCards, createCard, deleteCard, moveCard} from "./utils";

export default {
	name: "KanbanBoard",
	components: { Container, Draggable },
	mounted() {
		let cards = loadCards();
		cards.then(
			result => {
				if (result.RED) {
					this.RED = result.RED
					this.BLUE = result.BLUE
					this.YELLOW = result.YELLOW
					this.GREEN = result.GREEN
				}
			}
		)
			
	},
	data: function() {
		return {
			token: localStorage.getItem('token'),
			RED: [],
			BLUE: [],
			YELLOW: [],
			GREEN: [],
			newCardText: '',
			addACardStyle: [ 
					{ display: 'none'},
					{ display: 'none'},
					{ display: 'none'},
					{ display: 'none'} 
				],
			addAnotherCardStyle: [ 
					{ display: 'block'},
					{ display: 'block'},
					{ display: 'block'},
					{ display: 'block'}
				]
		};
	},
	methods: {
		onDrop: function(typeCard, dropResult) {
			this.hideAddACardTextarea();
			this[typeCard] = applyDrag(this[typeCard], dropResult);
			if (dropResult.addedIndex != null) {
				let card = dropResult.payload
				let newOrder = dropResult.addedIndex
				moveCard(card, typeCard, newOrder)
			}			
		},
		getChildPayload0: function(index) {
			return this.RED[index];
		},
		getChildPayload1: function(index) {
			return this.BLUE[index];
		},
		getChildPayload2: function(index) {
			return this.YELLOW[index];
		},
		getChildPayload3: function(index) {
			return this.GREEN[index];
		},
		addItem: function(typeCard) {
			if (this.newCardText) {
				let card = createCard(this.newCardText, typeCard)
				card.then(
					cardData => this[typeCard].push(cardData)
				)								

				this.hideAddACardTextarea();
			}
		},
		deleteItem: function(typeCard, item) {
			let index = this[typeCard].map(x => {
				return x.id;
			}).indexOf(item.id);
			
			this[typeCard].splice(index, 1);
			deleteCard(item.id)			
		},
		hideAddACardTextarea: function() {
			this.newCardText = '';
			for(let i = 0; i < this.addACardStyle.length; i++) {
				this.addACardStyle[i].display = 'none';
			}
			for(let i = 0; i < this.addAnotherCardStyle.length; i++) {
				this.addAnotherCardStyle[i].display = 'block';
			}
		},
		showAddACardTextarea: function(col) {
			this.hideAddACardTextarea();
			this.addAnotherCardStyle[col].display = 'none';
			this.addACardStyle[col].display = 'block';
			let textareaID = 'title' + col;

			setTimeout(function() {
				document.getElementById(textareaID).focus();
			}, 0);
		}
	}
};
</script>